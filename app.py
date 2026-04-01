import streamlit as st
import joblib
import numpy as np
import requests
import pandas as pd
# st.set_page_config(page_title="🎬 Movie Predictor", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ MUST BE FIRST
st.set_page_config(page_title="🎬 Movie Success Predictor", layout="centered")

# Load model
model = joblib.load("model.pkl")

# Title
st.markdown("<h1 style='text-align: center;'>🎬 Movie Success Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict HIT or FLOP using AI 🚀</p>", unsafe_allow_html=True)

# 🎯 --- API SECTION ---
import requests

# API_KEY = "your_actual_api_key_here"

movie_name = st.text_input("🎬 Enter Movie Name")

if st.button("Fetch Movie Data"):
    API_KEY = "2a4dc388"
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
    data = requests.get(url).json()

    st.write(data)

    if data["Response"] == "True":

        col1, col2 = st.columns([1,2])

    with col1:
        if data["Poster"] != "N/A":
            st.image(data["Poster"])

    with col2:
        st.subheader(data["Title"])
        st.write(f"⭐ Rating: {data['imdbRating']}")
        st.write(f"📅 Year: {data['Year']}")
        st.write(f"🎭 Genre: {data['Genre']}")
        st.write(f"📝 Plot: {data['Plot']}")

# 🎯 --- INPUTS ---
budget = st.number_input("💰 Budget (in millions)", min_value=1)
popularity = st.number_input("🔥 Popularity", min_value=0.0)
runtime = st.number_input("⏱ Runtime (minutes)", min_value=1)

features = np.array([[budget, popularity, runtime]])

# prediction = model.predict(features)
# proba = model.predict_proba(features)

if prediction[0] == 1:
    st.success("🎉 HIT!")
else:
    st.error("❌ FLOP")

st.write(f"🔥 Confidence: {proba[0][1]*100:.2f}%")

# 🎯 --- PREDICTION ---
if st.button("Predict"):
    prediction = model.predict(features)
    proba = model.predict_proba(features)

    if prediction[0] == 1:
        st.success("🎉 This movie will be a HIT!")
    else:
        st.error("❌ This movie may FLOP")

    st.write(f"🔥 Confidence: {proba[0][1]*100:.2f}%")

    # ✅ Confidence inside button
    confidence = proba[0][1]
    st.progress(confidence)
    st.info(f"🎯 Confidence: {confidence*100:.2f}%")

# 🎯 --- GRAPH SECTION ---
st.subheader("📊 Dataset Insights")

data = pd.read_csv("data/movies.csv")
st.line_chart(data["budget"])