"""
Car Dekho Market Trends Analysis
File: Car_Dekho_Analysis.py
Author: Your Name
Description: Exploratory Data Analysis & Depreciation Modeling on Used Cars Data
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ==========================================
# 1. Load Dataset
# ==========================================
df = pd.read_csv("1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv")

# ==========================================
# 2. Data Inspection
# ==========================================
print("Top 5 Rows:\n", df.head())
print("\nDataset Shape:", df.shape)
print("\nColumns:", df.columns.to_list())
print("\nData Summary:\n", df.describe(include="all").T)

# ==========================================
# 3. Data Cleaning & Feature Engineering
# ==========================================
# Drop duplicate records
print("Duplicate Rows Count:", df.duplicated().sum())
df = df.drop_duplicates().copy()

# Compute Vehicle Age, Absolute & Percentage Depreciation, and Brand
df["Vehicle_Age"] = 2018 - df["Year"]
df["Depreciation_Abs"] = df["Present_Price"] - df["Selling_Price"]
df["Depreciation_Pct"] = (df["Depreciation_Abs"] / df["Present_Price"]) * 100
df["Brand"] = df["Car_Name"].apply(lambda x: str(x).split()[0].lower())

# ==========================================
# 4. Core Statistical Answers
# ==========================================
print("\n=== CASE STUDY METRICS ===")
print(f"1. Year Range               : {df['Year'].min()} to {df['Year'].max()}")
print(f"2. Lowest Selling Price     : ₹{df['Selling_Price'].min()} Lakh")
print(f"3. Highest Selling Price    : ₹{df['Selling_Price'].max()} Lakhs")
print(f"4. Total Records            : {len(df)}")
print(f"5. Total Missing Values     : {df.isnull().sum().sum()}")
print(f"6. Unique Vehicles          : {df['Car_Name'].nunique()}")
print(
    f"7. Most Sold Vehicle        : {df['Car_Name'].mode()[0]} ({df['Car_Name'].value_counts().max()} records)"
)
print(f"8. CNG Vehicles Count       : {(df['Fuel_Type'] == 'CNG').sum()}")
print(f"9. Individual Sellers Count : {(df['Seller_Type'] == 'Individual').sum()}")
print(f"10. Automatic Vehicles Count: {(df['Transmission'] == 'Automatic').sum()}")
print(
    f"11. Single-Owner Vehicles   : {(df['Owner'] == 0).sum()} (Owner=0 denotes 1st owner)"
)

# Depreciation Extremes
most_dep = df.loc[df["Depreciation_Pct"].idxmax()]
least_dep = df.loc[df["Depreciation_Pct"].idxmin()]
print(
    f"\n12. Most Depreciated (%)   : {most_dep['Car_Name']} ({most_dep['Depreciation_Pct']:.2f}% lost)"
)
print(
    f"    Least Depreciated (%)  : {least_dep['Car_Name']} ({least_dep['Depreciation_Pct']:.2f}% lost)"
)

# Brand Retention Analysis
brand_retention = (
    df.groupby("Brand")
    .filter(lambda x: len(x) >= 3)
    .groupby("Brand")["Depreciation_Pct"]
    .mean()
    .sort_values()
)
print(
    "\n13. Top Retaining Brands (Lowest Avg % Loss):\n",
    brand_retention.head().round(2),
)

# Correlation Analysis
print("\n14. Depreciation Correlations:")
print(
    df[["Vehicle_Age", "Kms_Driven", "Present_Price", "Owner", "Depreciation_Pct"]]
    .corr()["Depreciation_Pct"]
    .round(3)
)

# ==========================================
# 5. Visualizations & Dashboard
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Car Dekho Market Trends Dashboard", fontsize=18)

# Chart 1: Vehicles by Fuel Type
df["Fuel_Type"].value_counts().plot(kind="bar", ax=axes[0, 0], color="skyblue")
axes[0, 0].set_title("1. Vehicles by Fuel Type", fontsize=12)
axes[0, 0].set_ylabel("Count")

# Chart 2: Vehicles by Seller Type
df["Seller_Type"].value_counts().plot(
    kind="bar", ax=axes[0, 1], color="salmon"
)
axes[0, 1].set_title("2. Vehicles by Seller Type", fontsize=12)
axes[0, 1].set_ylabel("Count")

# Chart 3: Price Distribution by Fuel Type
sns.boxplot(x="Fuel_Type", y="Selling_Price", data=df, ax=axes[1, 0])
axes[1, 0].set_title("3. Price Distribution by Fuel Type", fontsize=12)
axes[1, 0].set_ylabel("Selling Price (Lakhs)")

# Chart 4: Correlation Heatmap
sns.heatmap(
    df[
        [
            "Vehicle_Age",
            "Kms_Driven",
            "Present_Price",
            "Owner",
            "Depreciation_Pct",
        ]
    ].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=axes[1, 1],
)
axes[1, 1].set_title("4. Depreciation Drivers Heatmap", fontsize=12)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
