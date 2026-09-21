import streamlit as st
import csv
import os
from datetime import datetime
import pandas as pd
import plotly.express as px



st.set_page_config(page_title="AI Learning Assistant")
model_choice = st.selectbox(
    "Select Emotion Detection Model",
    ["BiLSTM", "BERT"]
)

st.title("🎓 AI Learning Assistant")
st.write("Emotion Detection & Personalized Learning Support")

problem = st.text_area("Describe your learning problem:")

if st.button("Analyze Emotion"):

    text = problem.lower()

    if "confused" in text or "don't understand" in text or "lost" in text:
        emotion = "Confused"

    elif "frustrated" in text or "angry" in text:
        emotion = "Frustrated"

    elif "interesting" in text or "curious" in text:
        emotion = "Curious"

    elif "confident" in text or "easy" in text:
        emotion = "Confident"

    elif "boring" in text or "bored" in text:
        emotion = "Bored"

    else:
        emotion = "Neutral"

    st.success("Emotion Detected")
    st.write("### Predicted Emotion")
    st.write(emotion)

    # CSV File
    file = "logs/history.csv"

    # Header create if file is empty
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        with open(file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Student Input", "Emotion"])

    # Save data
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), problem, emotion])

    st.success("Saved to history.csv")


   #model = genai.GenerativeModel("gemini-2.0-flash")

    #prompt = f"Student emotion: {emotion}. Student problem: {problem}. Give a short encouraging study suggestion."

    #response = model.generate_content(prompt)

    #st.write("### 🤖 AI Suggestion")
    #st.write(response.text)
    st.write("### 🤖 AI Suggestion")

    if emotion == "Confused":
        st.info("Don't worry! Learn one concept at a time and practice with simple examples.")

    elif emotion == "Frustrated":
        st.info("Take a short break and then try solving one small problem.")

    elif emotion == "Curious":
        st.info("Great! Keep exploring and learning new concepts.")

    elif emotion == "Confident":
        st.info("Excellent! Try solving more advanced questions.")

    elif emotion == "Bored":
        st.info("Watch a video or practice interactive exercises to make learning interesting.")

    else:
        st.info("Keep practicing every day. You are improving!")
    st.write("## 📊 Analytics Dashboard")

    df = pd.read_csv("logs/history.csv")

    fig = px.bar(
        df,
        x="Emotion",
        title="Emotion Distribution",
        color="Emotion"
    )

    st.plotly_chart(fig, use_container_width=True)
