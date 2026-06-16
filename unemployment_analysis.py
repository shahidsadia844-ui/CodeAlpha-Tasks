import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data (Apni csv file ka sahi path yahan likhen)
# Agar file same folder mein hai toh sirf naam kafi hai
try:
    df = pd.read_csv('unemployment.csv')
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Please check the dataset file path.")

# 2. Data Cleaning & Exploration
print("\n--- Data Head ---")
print(df.head())

print("\n--- Missing Values ---")
print(df.isnull().sum())

# Column ke names saaf karna (agar aaspas spaces hon)
df.columns = df.columns.str.strip()

# 3. Data Visualization (Trends over time)
plt.figure(figsize=(10, 5))
# Note: Apni CSV ke mutabiq 'Date' aur 'Estimated Unemployment Rate (%)' ke column names check kar lein
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df, marker='o', color='red')
plt.title('Unemployment Rate Trends')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('unemployment_trend.png') # Mobile par graph image save karne ke liye
print("Trend graph saved as unemployment_trend.png")

# 4. Covid-19 Impact Analysis (2020 ke dauran peak check karna)
plt.figure(figsize=(10, 5))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.title('Unemployment Rate by Region')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('region_wise_unemployment.png')
print("Region graph saved as region_wise_unemployment.png")
