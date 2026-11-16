# Import required libraries
import pandas as pd
from scipy.io import arff
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load ARFF file
data, meta = arff.loadarff('customers.arff')

# Step 2: Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Handle categorical/byte data (if any)
for col in df.select_dtypes([object]):
    df[col] = df[col].str.decode('utf-8')

# Step 4: Convert categorical data to numeric (if needed)
df = pd.get_dummies(df)

# Step 5: Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(df)

# Step 6: Display clustered data
print(df.head())

# Step 7: Visualize (first 2 features with actual names)

# Get feature names (excluding Cluster column)
feature_names = df.columns[:-1]

x_feature = feature_names[0]
y_feature = feature_names[1]

plt.scatter(df[x_feature], df[y_feature], c=df['Cluster'], cmap='viridis')

# Plot centroids
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='X')

plt.title("Customer Clusters")
plt.xlabel(x_feature)
plt.ylabel(y_feature)

plt.show()