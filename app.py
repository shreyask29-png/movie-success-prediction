import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("🎬 Movie Success Predictor")

budget = st.number_input("Budget")
popularity = st.number_input("Popularity")
runtime = st.number_input("Runtime")
vote = st.number_input("Vote Average")

if st.button("Predict"):
    data = pd.DataFrame({
        'budget': [budget],
        'popularity': [popularity],
        'runtime': [runtime],
        'vote_average': [vote]
    })

    result = model.predict(data)[0]

    if result == 1:
        st.success("Hit Movie 🎉")
    else:
        st.error("Flop Movie ❌")