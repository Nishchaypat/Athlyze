import streamlit as st
import json
import os

st.set_page_config(page_title="Athlyze | Nutrition Principles", page_icon="/Users/npatel237/Athlyze/backend/public/favicon.svg", layout="wide")

st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    .principle-card {
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border: 1px solid #e0e0e0;
    }
    .research-card {
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border: 1px solid #b6d4ff;
    }
    .section-header {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .stExpander {
        border: 1px solid #e0e0e0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

def load_training_principles():
    """Load the training principles from a JSON file or return default data."""
    file_path = "/Users/npatel237/Athlyze/backend/database/Nick_nutrition_principles.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {
        "hydration_guidelines": {
            "daily_water_intake": "Not specified",
            "timing_strategy": "Not specified",
            "explanation": "Not specified"
        },
        "adjustment_guidelines": {
            "weight_loss_plateau": "Not specified",
            "strength_plateau": "Not specified",
            "energy_issues": "Not specified"
        },
        "additional_recommendations_based_on_research": []
    }

def display_training_principles(principles):
    """Display training principles including hydration, adjustments, and research recommendations."""
    
    # Hydration Guidelines
    st.markdown("<h2>Hydration Guidelines</h2>", unsafe_allow_html=True)
    hydration_data = principles.get('hydration_guidelines', {})
    
    with st.expander("Daily Water Intake"):
        st.markdown(f"""
        <div class="principle-card">
            <p><strong>Recommended Intake:</strong> {hydration_data.get('daily_water_intake', 'N/A')}</p>
            <p><strong>Timing Strategy:</strong> {hydration_data.get('timing_strategy', 'N/A')}</p>
            <p><strong>Explanation:</strong> {hydration_data.get('explanation', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    # Adjustment Guidelines
    st.markdown("<h2>Adjustment Guidelines</h2>", unsafe_allow_html=True)
    adjustment_data = principles.get('adjustment_guidelines', {})
    
    for guideline, description in adjustment_data.items():
        with st.expander(guideline.replace('_', ' ').title()):
            st.markdown(f"""
            <div class="principle-card">
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)

    # Research-Based Recommendations
    st.markdown("<h2>Research-Based Recommendations</h2>", unsafe_allow_html=True)
    research_recommendations = principles.get('additional_recommendations_based_on_research', [])
    
    if research_recommendations:
        for recommendation in research_recommendations:
            with st.expander(recommendation.get('title', 'Untitled Recommendation')):
                st.markdown(f"""
                <div class="research-card">
                    <h4>{recommendation.get('title', 'Untitled')}</h4>
                    <p><strong>Description:</strong> {recommendation.get('description', 'N/A')}</p>
                    <p><strong>Scientific Basis:</strong> {recommendation.get('scientific_basis', 'N/A')}</p>
                    <p><strong>Implementation Strategy:</strong> {recommendation.get('implementation_strategy', 'N/A')}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("<p>No additional research-based recommendations available.</p>", unsafe_allow_html=True)

def main():
    """Main function to run the Streamlit app."""
    st.title("Nutrition Principles")
    training_principles = load_training_principles()
    display_training_principles(training_principles)

if __name__ == "__main__":
    main()
