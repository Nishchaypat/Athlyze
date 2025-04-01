import streamlit as st
import sys
import os
import time
import uuid
import extra_streamlit_components as stx
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from local_flows.nutrition_flow_local import run_the_flow as nutrition_flow
from local_flows.training_flow_local import run_the_flow as training_flow

st.set_page_config(page_title="Athlyze | Profile", page_icon="public/favicon.svg", layout="wide")

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

st.title("Your Profile")

st.subheader("Tell us about yourself:")
name = st.text_input("Name")
height = st.text_input("Height (ft' in'')", placeholder="5' 8''")
weight = st.text_input("Weight (lbs)", placeholder="150 lbs")
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

notes = "Name: " + name + "Height in ft, in: " + height + "Weight in lbs: "+ weight + "Age: " + str(age) + "Experience: " + experience + "Notes: " + notes

# Wrap your synchronous functions in async functions
async def async_nutrition_flow(name, notes, goals):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, nutrition_flow, name, notes, goals)

async def async_training_flow(name, notes, goals):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, training_flow, name, notes, goals)

async def run_flows_concurrently(name, notes, goals):
    # Run both flows concurrently and wait for them to finish
    nutrition_result, training_result = await asyncio.gather(
        async_nutrition_flow(name, notes, goals),
        async_training_flow(name, notes, goals)
    )
    return nutrition_result, training_result

if st.button("Generate My Plan"):
    st.success("Your personalized plan is being created...")
    try:
        with st.spinner("Analyzing your data..."):
            # Execute both flows in parallel
            status_nutrition, status_training = asyncio.run(run_flows_concurrently(name, notes, goals))

        if status_nutrition == "Success":
            st.subheader("Your AI-Powered Plan has been created")
            st.write("**Physical Training:** Check the Calendar")
            st.write("**Nutrition Plan:** Check the Nutrition") 
            st.write("Also, check the Training and Nutrition Principles")
    except Exception as e:
        st.error("Something went wrong. Please try again. Error: " + str(e))