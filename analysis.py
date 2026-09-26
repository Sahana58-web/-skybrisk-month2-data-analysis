import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- 1. Load the dataset ----
df = pd.read_csv("sales_data.csv")

print("Original data:")
print(df)
print("\nMissing values per column:")
print(df.isnull().sum())

# ---- 2. Clean the data ----
# Fill missing Quantity with the average quantity
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

# Fill missing Region with "Unknown" since we can't guess it
df["Region"] = df["Region"].fillna("Unknown")

print("\nCleaned data:")
print(df)

# Add a Total column (Quantity x Price) — useful for analysis
df["Total"] = df["Quantity"] * df["Price"]

# ---- 3. Basic analysis ----
print("\nAverage price by category:")
print(df.groupby("Category")["Price"].mean())

print("\nTotal sales by region:")
print(df.groupby("Region")["Total"].sum())

print("\nCorrelation between Quantity and Total:")
print(df[["Quantity", "Price", "Total"]].corr())

print("\nSummary statistics:")
print(df.describe())

# ---- 4. Visualizations ----
plt.figure(figsize=(6, 4))
sns.barplot(x="Category", y="Total", data=df, estimator=sum)
plt.title("Total Sales by Category")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(x="Region", y="Total", data=df, estimator=sum)
plt.title("Total Sales by Region")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

print("\nDone! Charts saved as sales_by_category.png and sales_by_region.png")