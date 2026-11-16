import pandas as pd
import numpy as np
from itertools import product

# ─────────────────────────────────────────────
# 1. Load dataset
# ─────────────────────────────────────────────
df = pd.read_csv('weather.csv', dtype=str)
print("=" * 60)
print("Weather Dataset")
print("=" * 60)
print(df.to_string(index=False))
print()

TARGET  = 'play'
FEATURES = [c for c in df.columns if c != TARGET]

class BayesianClassifier:
    def __init__(self, laplace=1):
        self.k = laplace
        self.prior        = {}   # P(C)
        self.joint_counts = {}   # count of (x1,x2,...,xn) in class C
        self.class_counts = {}   # |C|
        self.n_combos     = 0    # total unique feature combinations
        self.classes      = []

    def fit(self, X, y):
        self.classes = y.unique().tolist()
        n_total = len(y)

        # Total unique combinations across all feature values
        unique_vals = [X[f].unique().tolist() for f in X.columns]
        self.n_combos = 1
        for vals in unique_vals:
            self.n_combos *= len(vals)

        for cls in self.classes:
            subset = X[y == cls]
            self.class_counts[cls] = len(subset)
            self.prior[cls]        = len(subset) / n_total

            # Count each unique tuple occurrence within this class
            self.joint_counts[cls] = {}
            for _, row in subset.iterrows():
                key = tuple(row[f] for f in X.columns)
                self.joint_counts[cls][key] = \
                    self.joint_counts[cls].get(key, 0) + 1

    def _joint_likelihood(self, cls, sample_tuple):
        """P(x1,x2,...,xn | C)  with Laplace smoothing."""
        count = self.joint_counts[cls].get(sample_tuple, 0)
        return (count + self.k) / (self.class_counts[cls] + self.k * self.n_combos)

    def predict_proba(self, sample):
        sample_tuple = tuple(sample[f] for f in FEATURES)
        raw = {}
        for cls in self.classes:
            raw[cls] = self.prior[cls] * self._joint_likelihood(cls, sample_tuple)
        total = sum(raw.values())
        return {c: v / total for c, v in raw.items()}

    def predict(self, sample):
        return max(self.predict_proba(sample), key=lambda c: self.predict_proba(sample)[c])

# ─────────────────────────────────────────────
# 3. Train
# ─────────────────────────────────────────────
X = df[FEATURES]
y = df[TARGET]

model = BayesianClassifier(laplace=1)
model.fit(X, y)

# ─────────────────────────────────────────────
# 4. Prior probabilities
# ─────────────────────────────────────────────
print("=" * 60)
print("Prior Probabilities  P(play)")
print("=" * 60)
for cls in model.classes:
    n = model.class_counts[cls]
    print(f"  P(play={cls:3s}) = {model.prior[cls]:.4f}  ({n} / {len(df)})")
print()

# ─────────────────────────────────────────────
# 5. Joint Frequency Table  P(x1,x2,x3,x4 | C)
# ─────────────────────────────────────────────
print("=" * 60)
print("Joint Frequency Table  (count of each feature tuple per class)")
print(f"  Total unique combinations (|V|) = {model.n_combos}")
print(f"  Laplace smoothing: k = {model.k}")
print("=" * 60)

# Collect all tuples that appear in training data
all_tuples = sorted(set(
    tuple(row[f] for f in FEATURES)
    for _, row in df.iterrows()
))

print(f"\n  {'Outlook':<10} {'Temp':<8} {'Humidity':<10} {'Windy':<7}", end="")
for cls in model.classes:
    print(f"  count|{cls}  P(tuple|{cls})", end="")
print()
print("  " + "-" * 72)

for tup in all_tuples:
    print(f"  {tup[0]:<10} {tup[1]:<8} {tup[2]:<10} {tup[3]:<7}", end="")
    for cls in model.classes:
        cnt = model.joint_counts[cls].get(tup, 0)
        p   = model._joint_likelihood(cls, tup)
        print(f"    {cnt:>2}         {p:.4f}  ", end="")
    print()

# ─────────────────────────────────────────────
# 6. Predictions on training data
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("Predictions on Training Data")
print("=" * 60)
print(f"  {'#':<4} {'Outlook':<10} {'Temp':<8} {'Humidity':<10} "
      f"{'Windy':<7} {'Actual':<7} {'Predicted':<10} Correct")
print("  " + "-" * 66)

correct = 0
for i, row in df.iterrows():
    sample = {f: row[f] for f in FEATURES}
    proba  = model.predict_proba(sample)
    pred   = max(proba, key=proba.get)
    actual = row[TARGET]
    ok     = (pred == actual)
    if ok:
        correct += 1
    print(f"  {i+1:<4} {row['outlook']:<10} {row['temperature']:<8} "
          f"{row['humidity']:<10} {row['windy']:<7} {actual:<7} {pred:<10} {'Y' if ok else 'N'}")

accuracy = correct / len(df) * 100
print(f"\n  Training Accuracy: {correct}/{len(df)} = {accuracy:.1f}%")

# 7. Predict a new test sample — step-by-step

print("\n" + "=" * 60)
print("Predicting a New Sample  (Step-by-Step)")
print("=" * 60)

# Collect valid values for each feature from training data
valid = {f: sorted(df[f].unique().tolist()) for f in FEATURES}

print("  Enter values for each feature (case-sensitive):\n")
test = {}
for feat in FEATURES:
    options = ' / '.join(valid[feat])
    while True:
        val = input(f"  {feat} [{options}]: ").strip()
        if val in valid[feat]:
            test[feat] = val
            break
        print(f"    Invalid value. Choose from: {options}")

test_tuple = tuple(test[f] for f in FEATURES)

print(f"  Input: {test}\n")

for cls in model.classes:
    prior = model.prior[cls]
    joint = model._joint_likelihood(cls, test_tuple)
    numerator = prior * joint
    print(f"  Class = '{cls}'")
    print(f"    P(play={cls})              = {prior:.4f}")
    print(f"    P(tuple | play={cls})      = {joint:.6f}  "
          f"(count={model.joint_counts[cls].get(test_tuple,0)}, "
          f"smoothed: ({model.joint_counts[cls].get(test_tuple,0)}+{model.k}) "
          f"/ ({model.class_counts[cls]}+{model.k}*{model.n_combos}))")
    print(f"    P(play={cls}) x P(tuple|play={cls}) = {numerator:.6f}")
    print()

proba      = model.predict_proba(test)
prediction = max(proba, key=proba.get)

print("  Normalised posterior probabilities:")
for cls in sorted(proba):
    print(f"    P(play={cls} | sample) = {proba[cls]:.4f}")

print(f"\n  => Prediction: play = '{prediction}'")
print("=" * 60)

