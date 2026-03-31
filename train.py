import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/movies.csv")

df['success'] = df['revenue'].apply(lambda x: 1 if x > 100000000 else 0)

X = df[['budget', 'popularity', 'runtime', 'vote_average']]
y = df['success']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained!")