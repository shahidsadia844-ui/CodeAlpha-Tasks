import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

# 1. Generating Dummy Credit Dataset for Demonstration
np.random.seed(42)
n_samples = 1000

data = {
    'Income': np.random.normal(50000, 15000, n_samples),
    'Total_Debts': np.random.normal(15000, 8000, n_samples),
    'Payment_History_Score': np.random.randint(1, 10, n_samples), # 1 to 9 (Higher is better)
    'Age': np.random.randint(20, 65, n_samples),
    'Dependents': np.random.randint(0, 5, n_samples)
}

df = pd.DataFrame(data)

# Target Variable: Creditworthy (1 = Good, 0 = Bad risk) Based on basic financial logic
df['Creditworthy'] = np.where(
    (df['Income'] * df['Payment_History_Score'] / (df['Total_Debts'] + 1)) > 15, 1, 0
)

print("--- Dataset Sample ---")
print(df.head())

# 2. Feature Engineering: Debt-to-Income Ratio
df['Debt_to_Income_Ratio'] = df['Total_Debts'] / df['Income']

# 3. Splitting Features and Target
X = df.drop('Creditworthy', axis=1)
y = df['Creditworthy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Model Training (Using Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)
y_pred_prob = model.predict_proba(X_test_scaled)[:, 1]

# 5. Model Evaluation Metrics Assessment
print("\n--- Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\n--- Classification Report (Precision, Recall, F1-Score) ---")
print(classification_report(y_test, y_pred))

roc_auc = roc_auc_score(y_test, y_pred_prob)
print(f"ROC-AUC Score: {roc_auc:.4f}")

# Plotting ROC Curve (Optional: Save this image for GitHub)
fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.savefig('roc_curve.png') # Saves graph as image
plt.show()
