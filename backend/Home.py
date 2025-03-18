import streamlit as st

st.set_page_config(page_title="Athlyze", page_icon="/Users/npatel237/Athlyze/backend/public/favicon.svg", layout="wide")

st.title("Welcome to Athlyze! 🚀")
st.write("Navigate using the sidebar to explore different pages.")

feature_list = [
    ("🏋️ Personalized Training", "AI-powered workout plans based on scientific research, tailored to your goals."),
    ("🥗 Nutrition Planning", "Evidence-based nutrition strategies customized for optimal performance."),
    ("📅 Smart Calendar", "Intelligent scheduling adapts to your progress, preventing overtraining."),
    ("🤖 AI Coach", "Your fitness assistant answering questions with research-backed insights.")
]

for feature in feature_list:
    with st.expander(feature[0]):
        st.write(feature[1])