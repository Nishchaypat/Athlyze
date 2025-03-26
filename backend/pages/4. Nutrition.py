import streamlit as st
import json
import pandas as pd
import os
from datetime import datetime, timedelta
import calendar

st.set_page_config(page_title="Athlyze | Nutrition", page_icon="/Users/npatel237/Athlyze/backend/public/favicon.svg", layout="wide")

st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    .meal-card {
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

def load_nutrition_plan():
    """Load the nutrition plan from the JSON file."""
    try:
        file_path = "/Users/npatel237/Athlyze/backend/database/nutrition_plan.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            return {
                "intro": "Brief introduction summarizing the objectives and scope of the diet plan.",
                "diet_schedule": {
                    "caloric_needs": {
                        "daily_calories": "",
                        "calculation_method": "",
                        "adjustment_factors": ""
                    },
                    "macronutrient_distribution": {
                        "protein": "",
                        "carbohydrates": "",
                        "fats": "",
                        "explanation": ""
                    },
                    "daily_meal_plan": {
                        day: {
                            meal: {
                                "name": "",
                                "calories": "",
                                "macros": {"protein": "", "carbs": "", "fats": ""},
                                "ingredients": [],
                                "alternatives": []
                            } for meal in ["breakfast", "lunch", "pre_workout", "dinner"]
                        } for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                    }
                }
            }
    except Exception as e:
        st.error(f"Error loading nutrition plan: {e}")
        return None

def display_meal(meal_data, meal_name):
    """Display a single meal's details."""
    with st.container():
        st.markdown(f"""
        <div class="meal-card">
            <h4>{meal_data.get('name', meal_name)}</h4>
            <p><strong>Calories:</strong> {meal_data.get('calories', 'N/A')} | 
            <strong>Protein:</strong> {meal_data['macros'].get('protein', 'N/A')}g | 
            <strong>Carbs:</strong> {meal_data['macros'].get('carbs', 'N/A')}g | 
            <strong>Fats:</strong> {meal_data['macros'].get('fats', 'N/A')}g</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Details"):
            st.write("**Ingredients:**", ", ".join(meal_data.get('ingredients', [])) or "N/A")
            
            if meal_data.get('alternatives'):
                st.write("**Alternative Options:**")
                for alt in meal_data['alternatives']:
                    st.write(f"- {alt}")

def display_day_meals(day_meals, day_name):
    """Display the meal plan for a single day."""
    st.markdown(f"""
    <div class="day-header">
        <h3>{day_name}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for meal_name, meal_data in day_meals.items():
        display_meal(meal_data, meal_name)

def display_regular_view(nutrition_plan):
    """Display the nutrition plan in a tab view."""
    st.header("Weekly Nutrition Schedule")
    
    tabs = st.tabs(list(nutrition_plan["diet_schedule"]["daily_meal_plan"].keys()))
    
    for i, day in enumerate(nutrition_plan["diet_schedule"]["daily_meal_plan"]):
        with tabs[i]:
            display_day_meals(nutrition_plan["diet_schedule"]["daily_meal_plan"][day], day)

def display_calendar_view(nutrition_plan):
    """Display the nutrition plan in a calendar view."""
    st.header("Calendar View")
    
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    
    dates = [start_of_week + timedelta(days=i) for i in range(7)]
    date_strs = [d.strftime("%b %d") for d in dates]
    
    day_names = list(calendar.day_name)
    cols = st.columns(7)
    
    for i, (col, day_name, date_str) in enumerate(zip(cols, day_names, date_strs)):
        with col:
            day_data = nutrition_plan["diet_schedule"]["daily_meal_plan"].get(day_name, {})
            
            st.markdown(f"""
            <div class="calendar-header">
                {day_name}<br>{date_str}
            </div>
            """, unsafe_allow_html=True)
            
            if day_data:
                meal_count = len(day_data)
                
                st.markdown(f"""
                <div class="calendar-day">
                    <p><strong>Meals Planned:</strong> {meal_count}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if meal_count > 0:
                    with st.expander("View Meals"):
                        for meal_name, meal in day_data.items():
                            st.write(f"**{meal.get('name', meal_name)}**")
                            st.write(f"Calories: {meal.get('calories', 'N/A')} kcal")

def main():
    """Main function to run the Streamlit app."""
    st.title("Personalized Nutrition Plan")
    
    nutrition_plan = load_nutrition_plan()
    
    if not nutrition_plan:
        st.error("Failed to load nutrition plan. Please check the file path.")
        return
    
    st.markdown(f"### Introduction\n{nutrition_plan.get('intro', 'No introduction provided.')}")
    
    st.markdown("### **Caloric Needs & Macronutrient Distribution**")
    st.write(f"**Daily Calories:** {nutrition_plan['diet_schedule']['caloric_needs'].get('daily_calories', 'N/A')}")
    st.write(f"**Calculation Method:** {nutrition_plan['diet_schedule']['caloric_needs'].get('calculation_method', 'N/A')}")
    st.write(f"**Adjustment Factors:** {nutrition_plan['diet_schedule']['caloric_needs'].get('adjustment_factors', 'N/A')}")
    
    st.write("#### **Macronutrient Breakdown**")
    st.write(f"- **Protein:** {nutrition_plan['diet_schedule']['macronutrient_distribution'].get('protein', 'N/A')}%")
    st.write(f"- **Carbohydrates:** {nutrition_plan['diet_schedule']['macronutrient_distribution'].get('carbohydrates', 'N/A')}%")
    st.write(f"- **Fats:** {nutrition_plan['diet_schedule']['macronutrient_distribution'].get('fats', 'N/A')}%")
    st.write(f"**Explanation:** {nutrition_plan['diet_schedule']['macronutrient_distribution'].get('explanation', 'N/A')}")

    view_tab1, view_tab2 = st.tabs(["Regular View", "Calendar View"])
    
    with view_tab1:
        display_regular_view(nutrition_plan)
    
    with view_tab2:
        display_calendar_view(nutrition_plan)


if __name__ == "__main__":
    main()
