import streamlit as st
import json
import pandas as pd
import os
from datetime import datetime, timedelta
import calendar

# Set page config
st.set_page_config(
    page_title="Muscle Training Plan",
    page_icon="💪",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    .exercise-card {
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .day-header {
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .calendar-day {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        height: 100%;
    }
    .calendar-day:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .calendar-header {
        color: white;
        padding: 5px;
        border-radius: 5px 5px 0 0;
        text-align: center;
        font-weight: bold;
    }
    .rest-day {
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def load_training_plan():
    """Load the training plan from the JSON file."""
    try:
        file_path = "/Users/npatel237/Athlyze/sample_json/test1_flow.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            # If file doesn't exist, use the schema structure
            return {
                "intro": "A brief introduction summarizing the objectives and scope of the muscle training plan.",
                "training_schedule": {
                    "Monday": {"focus": "Example Focus", "exercises": []},
                    "Tuesday": {"focus": "Example Focus", "exercises": []},
                    "Wednesday": {"focus": "Example Focus", "exercises": []},
                    "Thursday": {"focus": "Example Focus", "exercises": []},
                    "Friday": {"focus": "Example Focus", "exercises": []},
                    "Saturday": {"focus": "Example Focus", "exercises": []},
                    "Sunday": {"focus": "Rest/Recovery", "recovery_protocols": {}}
                }
            }
    except Exception as e:
        st.error(f"Error loading training plan: {e}")
        return None

def display_exercise(exercise):
    """Display a single exercise with its details."""
    with st.container():
        st.markdown(f"""
        <div class="exercise-card">
            <h4>{exercise.get('name', 'Exercise Name')}</h4>
            <p><strong>Sets:</strong> {exercise.get('sets', 'N/A')} | 
            <strong>Reps:</strong> {exercise.get('reps', 'N/A')} | 
            <strong>Intensity:</strong> {exercise.get('intensity', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Details"):
            st.write("**Progression Strategy:**", exercise.get('progression_strategy', 'N/A'))
            st.write("**Scientific Explanation:**", exercise.get('scientific_explanation', 'N/A'))
            
            if exercise.get('alternatives'):
                st.write("**Alternatives:**")
                for alt in exercise['alternatives']:
                    st.write(f"- {alt.get('name', 'Alternative Exercise')}: {alt.get('reason_for_alternative', 'N/A')}")

def display_day_schedule(day_data, day_name):
    """Display the schedule for a single day."""
    st.markdown(f"""
    <div class="day-header">
        <h3>{day_name}: {day_data.get('focus', 'No focus specified')}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if day_name == "Sunday" and "recovery_protocols" in day_data:
        recovery = day_data["recovery_protocols"]
        st.write("**Recovery Protocols:**")
        cols = st.columns(2)
        with cols[0]:
            st.write("**Active Recovery:**", recovery.get('active_recovery', 'N/A'))
            st.write("**Stretching Routine:**", recovery.get('stretching_routine', 'N/A'))
        with cols[1]:
            st.write("**Mobility Drills:**", recovery.get('mobility_drills', 'N/A'))
            st.write("**Hydration and Nutrition:**", recovery.get('hydration_and_nutrition', 'N/A'))
    elif "exercises" in day_data:
        for exercise in day_data["exercises"]:
            display_exercise(exercise)

def display_regular_view(training_plan):
    """Display the training plan in a regular tab view."""
    st.header("Weekly Training Schedule")
    
    tabs = st.tabs(list(training_plan["training_schedule"].keys()))
    
    for i, day in enumerate(training_plan["training_schedule"]):
        with tabs[i]:
            display_day_schedule(training_plan["training_schedule"][day], day)

def display_calendar_view(training_plan):
    """Display the training plan in a calendar view."""
    st.header("Calendar View")
    
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    
    dates = [start_of_week + timedelta(days=i) for i in range(7)]
    date_strs = [d.strftime("%b %d") for d in dates]
    
    day_names = list(calendar.day_name)
    cols = st.columns(7)
    
    for i, (col, day_name, date_str) in enumerate(zip(cols, day_names, date_strs)):
        with col:
            day_data = training_plan["training_schedule"].get(day_name, {})
            
            st.markdown(f"""
            <div class="calendar-header">
                {day_name}<br>{date_str}
            </div>
            """, unsafe_allow_html=True)
            
            if day_name == "Sunday":
                st.markdown(f"""
                <div class="calendar-day rest-day">
                    <p><strong>Rest/Recovery</strong></p>
                    <p><small>Focus on recovery protocols</small></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                focus = day_data.get('focus', 'No focus')
                exercise_count = len(day_data.get('exercises', []))
                
                st.markdown(f"""
                <div class="calendar-day">
                    <p><strong>Focus:</strong> {focus}</p>
                    <p><small>{exercise_count} exercises</small></p>
                </div>
                """, unsafe_allow_html=True)
                
                if exercise_count > 0:
                    with st.expander("View Exercises"):
                        for exercise in day_data.get('exercises', []):
                            st.write(f"**{exercise.get('name', 'Exercise')}**")
                            st.write(f"{exercise.get('sets', '')} sets × {exercise.get('reps', '')} reps")

def main():
    """Main function to run the Streamlit app."""
    st.title("💪 Muscle Training Plan")
    
    training_plan = load_training_plan()
    
    if not training_plan:
        st.error("Failed to load training plan. Please check the file path.")
        return
    
    st.markdown(f"### Introduction\n{training_plan.get('intro', 'No introduction provided.')}")
    
    view_tab1, view_tab2 = st.tabs(["Regular View", "Calendar View"])
    
    with view_tab1:
        display_regular_view(training_plan)
    
    with view_tab2:
        display_calendar_view(training_plan)
    
    st.sidebar.header("Update Training Plan")
    uploaded_file = st.sidebar.file_uploader("Upload a new training plan (JSON)", type="json")
    
    if uploaded_file is not None:
        try:
            new_plan = json.load(uploaded_file)
            st.sidebar.success("File uploaded successfully! Click below to apply changes.")
            if st.sidebar.button("Apply Changes"):
                st.experimental_rerun()
        except Exception as e:
            st.sidebar.error(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
