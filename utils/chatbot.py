from langflow.load import run_flow_from_json
import os
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(GEMINI_API_KEY)
def read_files():
    """
    Reads files from the backend/database directory and aggregates JSON content
    into diet_plan and muscle_training variables based on file names.
    """
    diet_plan = []
    muscle_training = []

    for file in os.listdir("/Users/npatel237/Athlyze/backend/database"):
        file_path = os.path.join("backend/database", file)
        if os.path.isfile(file_path):
            if "nutrition" in file.lower():
                with open(file_path, 'r') as f:
                    diet_plan.append(json.load(f))
            elif "training" in file.lower():
                with open(file_path, 'r') as f:
                    muscle_training.append(json.load(f))

    return diet_plan, muscle_training

# Example usage
diet_plan, muscle_training = read_files()

TWEAKS = {
  "ChatOutput-ENBI5": {
    "background_color": "",
    "chat_icon": "",
    "clean_data": True,
    "data_template": "{text}",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "ChatInput-4XoLe": {
    "files": "",
    "background_color": "",
    "chat_icon": "",
    "input_value": "",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "TextInput-wddc6": {
    "input_value": "{diet_plan}"
  },
  "TextInput-GEX9L": {
    "input_value": "{muscle_training}"
  },
  "CombineText-hf6Eq": {
    "delimiter": " ",
    "text1": "",
    "text2": ""
  },
  "GoogleGenerativeAIModel-glg72": {
    "api_key": {GEMINI_API_KEY},
    "input_value": "",
    "max_output_tokens": None,
    "model_name": "gemini-2.5-pro-exp-03-25",
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
    "template": "Role:\nYou are an advanced AI specializing in personalized gym and nutrition planning. You have access to the user’s gym workout plan, diet schedule, fitness goals, and relevant health data.\n\nObjective:\nYour role is to provide expert-level guidance on workout routines, nutrition plans, and overall fitness optimization. You should tailor your responses based on the user’s specific plan, goals (e.g., muscle gain, fat loss, endurance improvement), dietary preferences, and any restrictions they may have.\n\nInstructions:\n\t•\tAnalyze the user’s existing gym plan and diet schedule before providing recommendations.\n\t•\tOffer evidence-based insights on fitness and nutrition, referencing scientific principles where applicable.\n\t•\tAdapt advice to align with the user’s goals, body composition, and progress.\n\t•\tProvide explanations in a clear, professional, and structured manner, ensuring that responses are actionable.\n\t•\tIf necessary, suggest modifications or improvements to optimize results while maintaining user safety and adherence.\n\nUser Engagement:\n\t•\tAnswer any questions related to workout techniques, recovery strategies, meal timing, macronutrient distribution, and supplementation.\n\t•\tOffer motivation and habit-building strategies to help users stay consistent.\n\t•\tProvide advanced recommendations if the user is at an intermediate or expert fitness level.",
    "tool_placeholder": ""
  }
}
    

result = run_flow_from_json(flow="/Users/npatel237/Athlyze/flow/ChatBot.json",
                            session_id="",
                            input_value="Describe me my diet plan and muscle training",
                            fallback_to_env_vars=True,
                            tweaks=TWEAKS)