import streamlit as st
import time
import sys
import os
import json
from dotenv import load_dotenv

# Add the backend directory to the path so we can import the Langflow function
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langflow.load import run_flow_from_json
import nest_asyncio
nest_asyncio.apply()

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

# Page configuration
st.set_page_config(
    page_title="Athlyze | Chat", 
    page_icon="favicon.svg", 
    layout="wide"
)

# App title and description
st.title("AI Fitness Coach")
st.write("Your personal AI assistant for fitness and nutrition guidance")

# Read database files
def read_files():
    """
    Reads files from the backend/database directory and aggregates JSON content
    into diet_plan and muscle_training variables based on file names.
    """
    diet_plan = []
    muscle_training = []

    for file in os.listdir("./database"):
        file_path = os.path.join("./database", file)
        if os.path.isfile(file_path):
            if "nutrition" in file.lower():
                with open(file_path, 'r') as f:
                    diet_plan.append(json.load(f))
            elif "training" in file.lower():
                with open(file_path, 'r') as f:
                    muscle_training.append(json.load(f))

    return diet_plan, muscle_training

# Get AI response function
def get_ai_response(user_message):
    """
    Gets AI response from Langflow for the user message
    """
    diet_plan, muscle_training = read_files()
    
    # Create a session ID based on current time to track conversation
    session_id = f"session_{int(time.time())}"
    
    # Configure tweaks for the Langflow model
    tweaks = {
        "ChatOutput-ENBI5": {
            "background_color": "",
            "chat_icon": "",
            "clean_data": True,
            "data_template": "text",
            "sender": "Machine",
            "sender_name": "AI",
            "session_id": session_id,
            "should_store_message": False,
            "text_color": ""
        },
        "ChatInput-4XoLe": {
            "files": "",
            "background_color": "",
            "chat_icon": "",
            "input_value": user_message,
            "sender": "User",
            "sender_name": "User",
            "session_id": session_id,
            "should_store_message": False,
            "text_color": ""
        },
        "TextInput-wddc6": {
            "input_value": json.dumps(diet_plan)
        },
        "TextInput-GEX9L": {
            "input_value": json.dumps(muscle_training)
        },
        "CombineText-hf6Eq": {
            "delimiter": " ",
            "text1": "",
            "text2": ""
        },
        "GoogleGenerativeAIModel-glg72": {
            "api_key": GEMINI_API_KEY,
            "input_value": "",
            "max_output_tokens": None,
            "model_name": "learnlm-1.5-pro-experimental",
            "n": None,
            "stream": False,
            "system_message": "",
            "temperature": 0.1,
            "tool_model_enabled": False,
            "top_k": None,
            "top_p": None
        },
        "CombineText-6LybF": {
            "delimiter": " ",
            "text1": "",
            "text2": ""
        },
        "Prompt-9iLne": {
            "template": "Role:\nYou are an advanced AI specializing in personalized gym and nutrition planning. You have access to the user's gym workout plan, diet schedule, fitness goals, and relevant health data.\n\nObjective:\nYour role is to provide expert-level guidance on workout routines, nutrition plans, and overall fitness optimization. You should tailor your responses based on the user's specific plan, goals (e.g., muscle gain, fat loss, endurance improvement), dietary preferences, and any restrictions they may have.\n\nInstructions:\n\t•\tAnalyze the user's existing gym plan and diet schedule before providing recommendations.\n\t•\tOffer evidence-based insights on fitness and nutrition, referencing scientific principles where applicable.\n\t•\tAdapt advice to align with the user's goals, body composition, and progress.\n\t•\tProvide explanations in a clear, professional, and structured manner, ensuring that responses are actionable.\n\t•\tIf necessary, suggest modifications or improvements to optimize results while maintaining user safety and adherence.\n\nUser Engagement:\n\t•\tAnswer any questions related to workout techniques, recovery strategies, meal timing, macronutrient distribution, and supplementation.\n\t•\tOffer motivation and habit-building strategies to help users stay consistent.\n\t•\tProvide advanced recommendations if the user is at an intermediate or expert fitness level.",
            "tool_placeholder": ""
        }
    }
    
    # Run the flow with the user message
    result = run_flow_from_json(
        flow="./flow/Chatbot.json",
        session_id=session_id,
        input_value=user_message,
        fallback_to_env_vars=True,
        tweaks=tweaks
    )

    return (dict(result[0].outputs[0].results['message'])['data']['text'])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How can I help with your fitness journey today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input area
if prompt := st.chat_input("Ask about your fitness plan..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(prompt)
            st.write(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Add some basic styling
st.markdown("""
<style>
    .stChatMessage {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    
    /* Custom header styling */
    .main .block-container {
        padding-top: 2rem;
    }
    
    h1 {
        color: #2E6E9E;
    }
</style>
""", unsafe_allow_html=True)