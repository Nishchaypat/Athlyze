import streamlit as st
import sys
import os
import time
import uuid
import concurrent.futures
import extra_streamlit_components as stx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from local_flows.nutrition_flow_local import run_the_flow as nutrition_flow
from local_flows.training_flow_local import run_the_flow as training_flow

st.set_page_config(page_title="Athlyze | Profile", page_icon="/Users/npatel237/Athlyze/backend/public/favicon.svg", layout="wide")

def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()

# Check if session_id exists in cookies
session_id = cookie_manager.get("session_id")

if session_id is None:
    session_id = str(uuid.uuid4())
    cookie_manager.set("session_id", session_id)

# Store session_id in session state for intra-page access
st.session_state["session_id"] = session_id


print("Profile Session ID::", session_id)

st.title("Your Profile")

st.subheader("Tell us about yourself:")
name = st.text_input("Name")
age = st.slider("Age", 16, 80, 20)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])

st.subheader("Make the description below as descriptive as possible:")

notes = st.text_area("Notes", placeholder=""" 
Dietary Notes: I am a pure vegetarian, my primary sources of protein are tofu, yogurt etc.
Activity: I am very active I want workout for 3 days a week. I have access to limited gym tools.
Possible Limitations: I cannot each soy, I have leg injury so I cannot do heavy leg workouts.""")

goals = st.text_area("Fitness Goal", placeholder="""Gain: I want to gain strength and some definition in my abs and legs. 
I really want to get good ass and butt. Lose: I want to lose fat in my thigh region, torso region, and my upper arm region""")

notes = "Name: " + name + "Age: " + str(age) + "Experience: " + experience + "Notes: " + notes

if st.button("Generate My Plan"):
    st.success("Your personalized plan is being created...")
    try:
        with st.spinner("Analyzing your data..."):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_nutrition = executor.submit(nutrition_flow, session_id, notes, goals)
                future_training = executor.submit(training_flow, session_id, notes, goals)

                status_nutrition = future_nutrition.result()
                status_training = future_training.result()


        if status_nutrition == "Success":
            st.subheader("Your AI-Powered Plan has been created")
            st.write("**Physical Training:** Check the Calendar")
            st.write("**Nutrition Plan:** Check the Nutrition")
            st.write("Also, check the Training and Nutrition Principles")
    except Exception as e:
        st.error("Something went wrong. Please try again. Error: " + str(e))