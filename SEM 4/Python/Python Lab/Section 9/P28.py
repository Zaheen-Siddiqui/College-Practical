# Title: Exploratory Data Analysis (EDA) using Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    # Load dataset
    df = pd.read_csv('your_dataset.csv')  # <-- Replace with your dataset
except FileNotFoundError:
    print("Error: The file 'your_dataset.csv' was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
    exit()
except pd.errors.ParserError:
    print("Error: Failed to parse CSV file.")
    exit()

try:
    # 1. Number of independent and dependent variables
    print("\nIndependent Variables:", list(df.columns[:-1]))
    print("Dependent Variable:", df.columns[-1])

    # 2. Display top 5 and last 5 rows
    print("\nTop 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())

    # 3. Display descriptive statistics
    print("\nDescriptive Statistics:\n", df.describe())

    # 4. Independent variable with minimum average value
    avg_values = df.mean(numeric_only=True)
    min_avg_col = avg_values.idxmin()
    print("\nIndependent Variable with Minimum Average Value:", min_avg_col)

    # 5. Independent variable with high standard deviation
    std_values = df.std(numeric_only=True)
    high_std_col = std_values.idxmax()
    print("\nIndependent Variable with Highest Standard Deviation:", high_std_col)

    # 6. Missing Values in each column
    print("\nMissing Values per Column:\n", df.isnull().sum())

    # Visualize missing values
    try:
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()
    except Exception as e:
        print("Error displaying heatmap:", e)

    # Column with maximum missing values
    max_missing_col = df.isnull().sum().idxmax()
    print("\nColumn with Maximum Missing Values:", max_missing_col)

    # 7. Replace missing values in one numeric column with average
    if pd.api.types.is_numeric_dtype(df[max_missing_col]):
        df[max_missing_col].fillna(df[max_missing_col].mean(), inplace=True)
        print(f"\nMissing values in '{max_missing_col}' filled with average.")
    else:
        print(f"\nColumn '{max_missing_col}' is not numeric, skipping imputation.")

    # 8. Frequency distribution using Histogram
    try:
        hist_col = df.select_dtypes(include=['float64', 'int64']).columns[0]
        df[hist_col].hist(bins=20)
        plt.title(f"Histogram of {hist_col}")
        plt.xlabel(hist_col)
        plt.ylabel("Frequency")
        plt.show()
    except IndexError:
        print("No numeric columns available for histogram.")

    # 9. Identify outliers using Boxplot
    try:
        plt.boxplot(df[hist_col])
        plt.title(f"Boxplot of {hist_col}")
        plt.show()
    except Exception as e:
        print("Error generating boxplot:", e)

    # 10. Correlation using Line Chart
    try:
        line_col = df.select_dtypes(include=['float64', 'int64']).columns[1]
        plt.plot(df[line_col])
        plt.title(f"Line Chart of {line_col}")
        plt.xlabel("Index")
        plt.ylabel(line_col)
        plt.show()
    except IndexError:
        print("Not enough numeric columns for line chart.")

    # 11. Correlation Matrix
    corr_matrix = df.corr(numeric_only=True)
    print("\nCorrelation Matrix:\n", corr_matrix)

    # Strongest correlation pairs
    corr_pairs = corr_matrix.unstack().sort_values()
    corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]  # Remove self-correlation

    if not corr_pairs.empty:
        print("\nStrongest Negative Correlation Pair:", corr_pairs.head(1))
        print("\nStrongest Positive Correlation Pair:", corr_pairs.tail(1))
    else:
        print("Correlation pairs not found.")

    # 12. Scatter plot between two columns
    try:
        columns = corr_matrix.columns
        plt.scatter(df[columns[0]], df[columns[1]])
        plt.title(f"Scatter Plot: {columns[0]} vs {columns[1]}")
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
        plt.show()
    except IndexError:
        print("Not enough columns for scatter plot.")
    except Exception as e:
        print("Error generating scatter plot:", e)

except Exception as e:
    print("An unexpected error occurred during analysis:", e)
