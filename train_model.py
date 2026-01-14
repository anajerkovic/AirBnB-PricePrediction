import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("airbnb_merged.csv")
df = df.drop(columns=["Unnamed: 0"])

y = df["realSum"]
X = df.drop(columns=["realSum"])

X = pd.get_dummies(X, columns=["room_type", "city"], drop_first=False)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

with open("randomforest_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model successfully trained and saved")
print("Number of features:", X.shape[1])
