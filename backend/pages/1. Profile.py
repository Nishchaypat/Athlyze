import streamlit as st
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from local_flows.nutrition_flow_local import run_the_flow 

st.set_page_config(page_title="Athlyze | Profile", page_icon="/Users/npatel237/Athlyze/backend/public/favicon.svg", layout="wide")
st.title("Your Profile")

st.subheader("Tell us about yourself:")
name = st.text_input("Name")
age = st.slider("Age", 16, 80, 20)
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])


notes = st.text_area("Notes", placeholder="""Demographic: I am a 22 year old female. I am approximately 4'11'' and 128 lbs.  
Dietary Notes: I am a pure vegetarian, my primary sources of protein are tofu, yogurt etc.
Activity: I am very active I want workout for 3 days a week. I have access to limited gym tools.
Possible Limitations: I cannot each soy, I have leg injury so I cannot do heavy leg workouts.""")

goals = st.text_area("Fitness Goal", placeholder="""Gain: I want to gain strength and some definition in my abs and legs. 
I really want to get good ass and butt. Lose: I want to lose fat in my thigh region, torso region, and my upper arm region""")

notes = "Name: " + name + "Age: " + str(age) + "Experience: " + experience + "Notes: " + notes

if st.button("Generate My Plan"):
    st.success("Your personalized plan is being created...")

    with st.spinner("Analyzing your data..."):
        status = run_the_flow(name, notes, goals)

    if status == "Success":
        st.subheader("Your AI-Powered Plan has been created")
        st.write("**Physical Training:** Check the Calendar")
        st.write("**Nutrition Plan:** Check the Nutrition")
        st.write("Also, check the Training and Nutrition Principles")
    else:
        st.error("Something went wrong. Please try again.")