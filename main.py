import streamlit as st
import glob as gb
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

filepaths = gb.glob('diary/*.txt')

positivity = []
negativity = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
        score = analyzer.polarity_scores(content)
    positivity.append(score['pos'])
    negativity.append(score['neg'])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.header("Diary Tone")
st.subheader("Positivity")

figure = px.line(x=dates,y=positivity, labels= {"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure2 =px.line(x=dates,y=negativity, labels= {"x": "Date", "y": "Negativity"})
st.plotly_chart(figure2)
