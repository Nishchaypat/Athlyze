import streamlit as st
import json
import os

st.set_page_config(page_title="Athlyze | Training Principles", page_icon="/Users/npatel237/Athlyze/backend/public/favicon.svg", layout="wide")

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

    file_path = "/Users/npatel237/Athlyze/backend/database/training_principle.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

def display_training_principles(principles):

    st.markdown("<h2>Core Training Principles</h2>", unsafe_allow_html=True)
    principles_data = principles.get('training_principles', {})
    
    for principle, description in principles_data.items():
        with st.expander(principle.replace('_', ' ').title()):
            st.markdown(f"""
            <div class="principle-card">
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<h2>Adjustment Guidelines</h2>", unsafe_allow_html=True)
    adjustment_data = principles.get('adjustment_guidelines', {})
    
    for guideline, description in adjustment_data.items():
        with st.expander(guideline.replace('_', ' ').title()):
            st.markdown(f"""
            <div class="principle-card">
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<h2>Performance Tracking</h2>", unsafe_allow_html=True)
    tracking_data = principles.get('performance_tracking', {})
    
    for metric, description in tracking_data.items():
        with st.expander(metric.replace('_', ' ').title()):
            st.markdown(f"""
            <div class="principle-card">
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<h2>Research-Based Recommendations</h2>", unsafe_allow_html=True)
    research_recommendations = principles.get('additional_recommendations_based_on_research', [])
    
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

def main():
    """Main function to run the Streamlit app."""
    st.title("Muscle Training Principles")
    training_principles = load_training_principles()
    display_training_principles(training_principles)

if __name__ == "__main__":
    main()