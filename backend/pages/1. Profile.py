import streamlit as st
import time

st.set_page_config(page_title="Athlyze | Profile", page_icon="/Users/npatel237/Athlyze/backend/public/favicon.svg", layout="wide")
st.title("Your Profile")

st.subheader("Tell us about yourself:")
age = st.slider("Age", 16, 80, 20)
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])

notes = st.text_area("Notes", placeholder="""Demographic: I am a 22 year old female. I am approximately 4'11'' and 128 lbs.  
Dietary Notes: I am a pure vegetarian, my primary sources of protein are tofu, yogurt etc.
Activity: I am very active I want workout for 3 days a week. I have access to limited gym tools.""")

goal = st.text_area("Fitness Goal", placeholder="""Gain: I want to gain strength and some definition in my abs and legs. 
I really want to get good ass and butt. Lose: I want to lose fat in my thigh region, torso region, and my upper arm region""")


if st.button("Generate My Plan"):
    st.success("Your personalized plan is being created...")

    with st.spinner("Analyzing your data..."):
        time.sleep(2)

    st.subheader("Your AI-Powered Plan")
    st.write(f"🎯 **Goal:** {goal}")
    st.write(f"🔥 **Experience Level:** {experience}")
    st.write(f"🚧 **Limitations:** {limitations if limitations else 'None'}")
    st.write("Your training and nutrition plan has been tailored to your needs.")