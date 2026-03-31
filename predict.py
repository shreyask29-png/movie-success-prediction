import joblib

model = joblib.load("model.pkl")

# Example movie input
result = model.predict([[50000000, 80, 120, 7.5]])

print("Prediction:", "Hit 🎉" if result[0] == 1 else "Flop ❌")