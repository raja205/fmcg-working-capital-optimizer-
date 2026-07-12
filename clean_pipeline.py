import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Load Data
df = pd.read_csv('fmcg_invoice_data.csv')

# 2. Select Non-leaky Features (We do not include payment_date or days_taken_to_pay because they are unknown when issuing an invoice!)
X = df[['invoice_amount', 'allowed_terms']]
# One-hot encode categorical string features cleanly
X = pd.concat([X, pd.get_dummies(df[['distributor_name', 'sku_category']])], axis=1)
y = df['is_delinquent']

# 3. Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_test_split=0.2, random_state=42)

# 4. Fit Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Predict and Evaluate
predictions = model.predict(X_test)
print(f"Overall Model Accuracy: {accuracy_score(y_test, predictions):.2%}\n")
print(classification_report(y_test, predictions))

