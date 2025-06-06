import streamlit as st
import os

st.set_page_config(page_title="Athlyze", page_icon="public/favicon.svg", layout="wide")

# Custom CSS for improved styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    local_css("styles.css")
except FileNotFoundError:
    pass

# Main Page Design
def main():
    # Custom header with gradient and logo potential
    st.markdown("""
    <div style="background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%); 
                padding: 20px; 
                border-radius: 10px; 
                color: white; 
                text-align: center;">
        <h1 style="margin-bottom: 10px;">🏋️ Athlyze: Your AI Fitness Companion</h1>
        <p>Revolutionizing personal fitness through intelligent, personalized guidance</p>
    </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("## Key Features")
    
    features = [
        {
            "icon": "🏋️",
            "title": "Personalized Training",
            "description": "AI-powered workout plans based on scientific research, tailored to your unique fitness goals and body type.",
            "details": [
                "Adaptive workout recommendations",
                "Progress tracking",
                "Machine learning-driven improvements"
            ]
        },
        {
            "icon": "🥗",
            "title": "Nutrition Planning",
            "description": "Evidence-based nutrition strategies customized for optimal performance and individual metabolic needs.",
            "details": [
                "Personalized meal plans",
                "Macro and micronutrient tracking",
                "Dietary goal alignment"
            ]
        },
        {
            "icon": "📅",
            "title": "Smart Calendar",
            "description": "Intelligent scheduling that adapts to your progress, preventing overtraining and optimizing recovery.",
            "details": [
                "Automatic workout scheduling",
                "Rest day recommendations",
                "Dynamic plan adjustments"
            ]
        },
        {
            "icon": "🤖",
            "title": "AI Coach",
            "description": "Your 24/7 fitness assistant providing research-backed insights and personalized guidance.",
            "details": [
                "Real-time fitness queries",
                "Form correction suggestions",
                "Motivational support"
            ]
        }
    ]

    # Create a 2x2 grid for features
    cols = st.columns(2)
    
    for i, feature in enumerate(features):
        with cols[i // 2]:
            with st.expander(f"{feature['icon']} {feature['title']}", expanded=True):
                st.markdown(f"**{feature['description']}**")
                st.markdown("Key Capabilities:")
                for detail in feature['details']:
                    st.markdown(f"- {detail}")

if __name__ == "__main__":
    main()
