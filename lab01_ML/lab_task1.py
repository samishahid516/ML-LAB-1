"""
AIC-301 Machine Learning Lab - Lab # 01
Lab Task 1: Pandas Data Exploration
Dataset: Pakistan Average Temperature 1901-2016 (Kaggle)
"""

import pandas as pd

df = pd.read_csv("Tempreture_1901_2016_Pakistan.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "").str.replace("(", "").str.replace(")", "")
df.rename(columns={"temperature__celsius": "temperature"}, inplace=True)

print("Cleaned columns:", df.columns.tolist())
print("\n--- First 5 rows (df.head()) ---\n", df.head())
print("\n--- Missing values per column (df.isnull().sum()) ---\n", df.isnull().sum())
print("\n--- Summary statistics (df.describe()) ---\n", df.describe())

stats = {"Mean": df["temperature"].mean(), "Median": df["temperature"].median(), "Max": df["temperature"].max(), "Min": df["temperature"].min()}
for k, v in stats.items(): print(f"{k} temperature: {v:.2f} C")

summer_df = df[df["month"].isin(["June", "July", "August"])]
print(f"\nAverage summer (Jun-Aug) temperature: {summer_df['temperature'].mean():.2f} C")

hot_recent = df[(df["year"] > 2000) & (df["temperature"] > 25)]
print(f"Records after 2000 with temp > 25C: {len(hot_recent)} rows\n", hot_recent.head())

print("\n--- Temperature data for 2015 and 2016 ---")
print(df[df["year"].isin([2015, 2016])])

year