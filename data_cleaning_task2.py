import pandas as pd
import numpy as np

# 1. Generating a Messy Raw Dataset for Demonstration
raw_data = {
    'PassengerId': [101, 102, 103, 104, 104, 105, 106, 107], # 104 is duplicated
    'Name': ['Alice Smith', 'Bob Jones', 'Charlie Brown', 'Diana Prince', 'Diana Prince', 'Evan Wright', 'Fiona Gallagher', 'George Clark'],
    'Age': [25, np.nan, 32, 28, 28, 150, 22, np.nan],        # Has NaN values and an outlier (150)
    'Join_Date': ['2026-01-15', '2026/02/20', '2026-03-01', '04-12-2026', '04-12-2026', '2026-05-18', '2026-06-01', '2026-06-12'], # Messy date formats
    'Salary': ['₹50,000', '₹60,000', '₹45,000', '₹80,000', '₹80,000', '₹55,000', '₹1,200,000', '₹62,000'] # Strings with currency symbols and outlier
}

df = pd.DataFrame(raw_data)
print("--- ORIGINAL UNCLEANED DATASET ---")
print(df)
print("\n" + "="*50 + "\n")

# 2. Handling Duplicate Rows
print("Step 1: Removing Duplicate Entries...")
df = df.drop_duplicates()
print(f"Dataset size after removing duplicates: {df.shape}")

# 3. Data Type Conversions & Standardizing Formats
print("\nStep 2: Correcting Data Types and Formats...")
# Cleaning Salary: Removing currency symbols and commas, then converting to numeric
df['Salary'] = df['Salary'].str.replace('₹', '').str.replace(',', '').astype(float)

# Cleaning Join_Date: Parsing messy strings into standardized datetime format
df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')

# 4. Handling Missing Values (Imputation)
print("\nStep 3: Imputing Missing Values (NaN)...")
# Filling missing Age values with the median age of the group
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# 5. Outlier Detection and Treatment
print("\nStep 4: Detecting and Fixing Outliers...")
# Age 150 is structurally impossible, cap it or replace with median
df.loc[df['Age'] > 100, 'Age'] = median_age

# Salary outlier handling using Interquartile Range (IQR) thresholding
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + (1.5 * IQR)

# If salary is greater than upper bound, cap it at upper bound limit
df.loc[df['Salary'] > upper_bound, 'Salary'] = upper_bound

# 6. Final Cleaned Output
print("\n" + "="*50 + "\n")
print("--- FINAL CLEANED AND PREPARED DATASET ---")
print(df)

# Exporting clean data to csv template
df.to_csv('cleaned_dataset.csv', index=False)
print("\nCleaned data successfully exported to 'cleaned_dataset.csv'")
