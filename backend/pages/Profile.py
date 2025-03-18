import streamlit as st
import time

st.title("💪 Transform Your Physique with Science and AI")
st.write("Athlyze combines AI with scientific research to create personalized training and nutrition plans.")

# User Profile Inputs
st.subheader("Tell us about yourself:")
age = st.slider("Age", 16, 80, 25)
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
goal = st.selectbox("Fitness Goal", ["Muscle Gain", "Weight Loss", "Strength Training", "Endurance"])
limitations = st.text_area("Limitations (e.g., injuries, dietary restrictions)")

if st.button("Generate My Plan"):
    st.success("Your personalized plan is being created...")

    with st.spinner("Analyzing your data..."):
        time.sleep(2)

    st.subheader("Your AI-Powered Plan")
    st.write(f"🎯 **Goal:** {goal}")
    st.write(f"🔥 **Experience Level:** {experience}")
    st.write(f"🚧 **Limitations:** {limitations if limitations else 'None'}")
    st.write("Your training and nutrition plan has been tailored to your needs.")