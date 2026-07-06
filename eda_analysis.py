import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_excel("Dataset for Data Analytics.xlsx")
# Create Graphs Folder
os.makedirs("Graphs", exist_ok=True)
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

# Dataset Shape
print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

# Column Names
print("\nColumns:")
print(df.columns.tolist())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

print("\n" + "=" * 50)
print("BASIC STATISTICS")
print("=" * 50)

# Numerical Columns Statistics
print("\nStatistical Summary:")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean(numeric_only=True))

# Median
print("\nMedian:")
print(df.median(numeric_only=True))

# Standard Deviation
print("\nStandard Deviation:")
print(df.std(numeric_only=True))



#..............................
print("\n" + "=" * 50)
print("TREND ANALYSIS")
print("=" * 50)

# Most Sold Product
print("\nMost Sold Products:")
print(df["Product"].value_counts())

# Payment Method Distribution
print("\nPayment Method Distribution:")
print(df["PaymentMethod"].value_counts())

# Order Status Distribution
print("\nOrder Status Distribution:")
print(df["OrderStatus"].value_counts())

# Referral Source Distribution
print("\nReferral Source Distribution:")
print(df["ReferralSource"].value_counts())

# Average Order Value
print("\nAverage Order Value:")
print(round(df["TotalPrice"].mean(), 2))


#........
print("\n" + "=" * 50)
print("DISTRIBUTION ANALYSIS")
print("=" * 50)

# Histogram for Total Price
plt.figure(figsize=(8,5))
plt.hist(df["TotalPrice"], bins=20, edgecolor="black")
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("Graphs/TotalPrice_Histogram.png")
plt.show()

# Histogram for Quantity
plt.figure(figsize=(8,5))
plt.hist(df["Quantity"], bins=10, edgecolor="black")
plt.title("Distribution of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("Graphs/Quantity_Histogram.png")
plt.show()

#......
print("\n" + "=" * 50)
print("OUTLIER DETECTION")
print("=" * 50)

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["TotalPrice"] < lower) | (df["TotalPrice"] > upper)]

print(f"Total Outliers Found: {len(outliers)}")

# Box Plot
plt.figure(figsize=(8,5))
plt.boxplot(df["TotalPrice"], vert=False)
plt.title("Outlier Detection - Total Price")
plt.xlabel("Total Price")
plt.savefig("Graphs/TotalPrice_Boxplot.png")
plt.show()

#....
print("\n" + "=" * 50)
print("BAR CHARTS")
print("=" * 50)

# Product Distribution
plt.figure(figsize=(8,5))
df["Product"].value_counts().plot(kind="bar")
plt.title("Product Distribution")
plt.xlabel("Product")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Graphs/Product_Distribution.png")
plt.show()

# Payment Method Distribution
plt.figure(figsize=(8,5))
df["PaymentMethod"].value_counts().plot(kind="bar")
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Graphs/Payment_Method_Distribution.png")
plt.show()

#...........
print("\n" + "=" * 50)
print("GENERATING EDA REPORT")
print("=" * 50)

summary = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Average Total Price",
        "Median Total Price",
        "Highest Selling Product",
        "Most Used Payment Method",
        "Most Common Order Status",
        "Most Common Referral Source",
        "Total Outliers"
    ],
    "Value": [
        df.shape[0],
        df.shape[1],
        round(df["TotalPrice"].mean(),2),
        round(df["TotalPrice"].median(),2),
        df["Product"].value_counts().idxmax(),
        df["PaymentMethod"].value_counts().idxmax(),
        df["OrderStatus"].value_counts().idxmax(),
        df["ReferralSource"].value_counts().idxmax(),
        len(outliers)
    ]
})

summary.to_excel("EDA_Report.xlsx", index=False)

print("\nEDA Report Generated Successfully!")
print("Saved as : EDA_Report.xlsx")