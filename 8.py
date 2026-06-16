import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Data
try:
    df = pd.read_csv('car_data.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Please check the dataset file path.")

# Data ki columns dekhne ke liye
print(df.head())
print(df.info())

# 2. Data Preprocessing & Feature Selection
# Note: Kaggle ke datasets mein aam tor par yeh columns hoti hain. 
# Agar aapke dataset mein names thode badal kar hon, toh unhe check kar lein.
# Hum text data (categorical) ko drop kar ke sirf numeric features le rahe hain aasan rkhne ke liye:
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Agar columns mein missing values hon toh unhe fill karna
numeric_df = numeric_df.fillna(numeric_df.mean())

# Target variable (Y) jo predict karna hai, aur Features (X) jis ki bunyad par predict karna hai
# Aam tor par column ka naam 'Selling_Price' ya 'price' hota hai
target_col = [col for col in numeric_df.columns if 'price' in col.lower() or 'selling' in col.lower()][0]

X = numeric_df.drop(columns=[target_col])
y = numeric_df[target_col]

# 3. Train-Test Split (80% data training ke liye, 20% testing ke liye)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_test_split=0.2, random_state=42)

# 4. Model Training (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained successfully!")

# 5. Model Evaluation (Testing)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n--- Model Evaluation ---")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score (Accuracy): {r2*100:.2f}%")

# 6. Visualization (Actual vs Predicted Prices Graph)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Car Prices')
plt.tight_layout()
plt.savefig('actual_vs_predicted.png')
print("Evaluation graph saved as actual_vs_predicted.png")
