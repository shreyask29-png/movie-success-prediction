import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("data/movies.csv")

print(df.columns)

# Create target column
df['success'] = df['revenue'].apply(lambda x: 1 if x > 100000000 else 0)

# Features & Target
# X = df[['budget', 'rating', 'votes']]   # input features
X = df[['budget', 'popularity', 'runtime']]
y = df['success']                       # output

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved successfully!")
