import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

print("=== TASK 3: Predictive Analytics ===")

np.random.seed(42)

data = pd.DataFrame({
    "failed_logins": np.random.randint(0, 10, 200),
    "ip_risk_score": np.random.randint(10, 100, 200),
    "time_of_day": np.random.randint(0, 24, 200),
})

data["is_attack"] = ((data["failed_logins"] > 4) | (data["ip_risk_score"] > 70)).astype(int)

print("Dataset created.")
print("Head of data:")
print(data.head())

X = data[["failed_logins", "ip_risk_score", "time_of_day"]]
y = data["is_attack"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)
print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, pred))
