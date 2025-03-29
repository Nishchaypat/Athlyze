from langflow.load import run_flow_from_json
import os
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

def save_json_data(data, filename, path="/Users/npatel237/Athlyze/backend/database"):
  """
  Save JSON data with robust error handling and logging
  """
  try:
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, filename)

    if isinstance(data, str):
      data = data.strip().replace('``````', '').strip()
    
    try:
      parsed_data = json.loads(data) if isinstance(data, str) else data
    except json.JSONDecodeError:
      parsed_data = data

    with open(file_path, 'w') as f:
      json.dump(parsed_data, f, indent=2)
        
  except Exception as e:
    raise(f"Error saving JSON data: {e}")
  
def run_the_flow(name, notes, goals):

  TWEAKS = {
    "GoogleGenerativeAIModel-tmINJ": {
        "api_key": GEMINI_API_KEY,
        "input_value": "",
        "max_output_tokens": None,
        "model_name": "gemini-2.0-flash-thinking-exp-1219",
        "n": None,
        "stream": False,
        "system_message": "Convert the provided user information into at least five diverse and precise search queries for retrieving relevant muscle training research papers vector database. Ensure the queries cover different aspects such as training techniques, recovery methods, injury prevention, progressive overload ensuring muscle growth. Return only the generated text queries in a single paragraph, separated by periods, without any additional text or explanations.\n\n{profile}",
        "temperature": 0.1,
        "tool_model_enabled": False,
        "top_k": None,
        "top_p": None
    },
    "AstraDB-wHLrw": {
        "advanced_search_filter": "{}",
        "api_endpoint": "https://4b6b6aaa-81eb-4706-9e80-6af3d6a3a7c6-us-east1.apps.astra.datastax.com",
        "astradb_vectorstore_kwargs": "{}",
        "autodetect_collection": True,
        "collection_name": "muscle_research_collection",
        "content_field": "",
        "database_name": "muscle_research_papers",
        "deletion_field": "",
        "embedding_choice": "Embedding Model",
        "environment": "",
        "ignore_invalid_documents": False,
        "keyspace": "",
        "number_of_results": 15,
        "search_query": "",
        "search_score_threshold": 0.7,
        "search_type": "Similarity",
        "should_cache_vector_store": True,
        "token": ASTRA_DB_APPLICATION_TOKEN
    },
    "Google Generative AI Embeddings-BZcXc": {
        "api_key": GEMINI_API_KEY,
        "model_name": "models/text-embedding-004"
    },
    "Prompt-DQWlH": {
        "template": "You are an expert fitness trainer specializing in evidence-based training planner. Using the scientific research provided below, create a comprehensive, personalized training plan that fits User Profile and the research data\n\nRESEARCH DATABASE:\n{muscle_data}\n\nUSER PROFILE:\n- Notes: {notes}\n- Goals: {goals}\n\nINSTRUCTIONS:\n1. Analyze the user's notes and goals to create a fully personalized plan\n2. Base all recommendations on scientific evidence from the provided research\n3. Include clear explanations for why each exercise recommendation was selected\n4. Provide detailed instructions for proper exercise technique\n5. Design a progressive plan that adapts over time as the user advances\n6. Include strategies for tracking progress and making adjustments when needed\n7. Consider any health conditions or limitations mentioned in the user notes\n\nYour response should be comprehensive, scientifically sound, and practical for implementation.\n\nVery Important: Make sure to return the response without any ```json```.\n",
        "tool_placeholder": "",
        "notes": "",
        "goals": "",
        "muscle_data": ""
    },
    "ParseData-PBC9c": {
        "sep": "\n",
        "template": "{text}"
    },
    "GoogleGenerativeAIModel-EmX6l": {
        "api_key": GEMINI_API_KEY,
        "input_value": "",
        "max_output_tokens": 40000000,
        "model_name": "gemini-2.0-flash-thinking-exp-01-21",
        "n": None,
        "stream": False,
        "system_message": "You are an advanced AI assistant specialized in creating scientifically-backed fitness plans. Your task is to generate a comprehensive Training Plan structured precisely according to the provided JSON schema. Provide only JSON-formatted output strictly matching this schema, without additional explanations or commentary. \n\nVery Important: Make sure to return the response without any ```json```.\n\nAt most give 3 exercises per day.\n\nSchema:\n\n{\n  \"intro\": \"A brief introduction summarizing the objectives and scope of the muscle training plan.\",\n  \"training_schedule\": {\n    \"Monday\": {\n      \"focus\": \"\",\n      \"exercises\": [\n        {\n          \"name\": \"\",\n          \"sets\": \"\",\n          \"reps\": \"\",\n          \"intensity\": \"\",\n          \"progression_strategy\": \"\",\n          \"scientific_explanation\": \"\",\n          \"alternatives\": [\n            {\n              \"name\": \"\",\n              \"reason_for_alternative\": \"\"\n            }\n          ]\n        }\n      ]\n    },\n    \"Tuesday\": {\n      \"focus\": \"\",\n      \"exercises\": [\n        {\n          \"name\": \"\",\n          \"sets\": \"\",\n          \"reps\": \"\",\n          \"intensity\": \"\",\n          \"progression_strategy\": \"\",\n          \"scientific_explanation\": \"\",\n          \"alternatives\": [\n            {\n              \"name\": \"\",\n              \"reason_for_alternative\": \"\"\n            }\n          ]\n        }\n      ]\n    },\n    \"Wednesday\": {\n      \"focus\": \"\",\n      \"exercises\": [\n        {\n          \"name\": \"\",\n          \"sets\": \"\",\n          \"reps\": \"\",\n          \"intensity\": \"\",\n          \"progression_strategy\": \"\",\n          \"scientific_explanation\": \"\",\n          \"alternatives\": [\n            {\n              \"name\": \"\",\n              \"reason_for_alternative\": \"\"\n            }\n          ]\n        }\n      ]\n    },\n    \"Thursday\": {\n      \"focus\": \"\",\n      \"exercises\": [\n        {\n          \"name\": \"\",\n          \"sets\": \"\",\n          \"reps\": \"\",\n          \"intensity\": \"\",\n          \"progression_strategy\": \"\",\n          \"scientific_explanation\": \"\",\n          \"alternatives\": [\n            {\n              \"name\": \"\",\n              \"reason_for_alternative\": \"\"\n            }\n          ]\n        }\n      ]\n    },\n    \"Friday\": {\n      \"focus\": \"\",\n      \"exercises\": [\n        {\n          \"name\": \"\",\n          \"sets\": \"\",\n          \"reps\": \"\",\n          \"intensity\": \"\",\n          \"progression_strategy\": \"\",\n          \"scientific_explanation\": \"\",\n          \"alternatives\": [\n            {\n              \"name\": \"\",\n              \"reason_for_alternative\": \"\"\n            }\n          ]\n        }\n      ]\n    },\n    \"Saturday\": {\n      \"focus\": \"\",\n      \"exercises\": [\n        {\n          \"name\": \"\",\n          \"sets\": \"\",\n          \"reps\": \"\",\n          \"intensity\": \"\",\n          \"progression_strategy\": \"\",\n          \"scientific_explanation\": \"\",\n          \"alternatives\": [\n            {\n              \"name\": \"\",\n              \"reason_for_alternative\": \"\"\n            }\n          ]\n        }\n      ]\n    },\n    \"Sunday\": {\n      \"focus\": \"Rest/Recovery\",\n      \"recovery_protocols\": {\n        \"active_recovery\": \"\",\n        \"stretching_routine\": \"\",\n        \"mobility_drills\": \"\",\n        \"hydration_and_nutrition\": \"\"\n      }\n    }\n  }\n}\n",
        "temperature": 1,
        "tool_model_enabled": False,
        "top_k": None,
        "top_p": None
    },
    "TextInput-E61Zz": {
        "input_value": notes
    },
    "TextInput-rZv5l": {
        "input_value": goals
    },
    "TextOutput-FoYjn": {
        "input_value": ""
    },
    "GoogleGenerativeAIModel-ekoqV": {
        "api_key": GEMINI_API_KEY,
        "input_value": "",
        "max_output_tokens": 400000,
        "model_name": "gemini-2.0-flash-thinking-exp-01-21",
        "n": None,
        "stream": False,
        "system_message": "You are an advanced AI assistant specialized in creating scientifically-backed fitness principles. Your task is to generate a comprehensive training principles, guidelines, and recommendations. All content should reflect the provided research data in the prompt. Provide only JSON-formatted output strictly matching this schema, without additional explanations or commentary:\n\nVery Important: Make sure to return the response without any ```json```.\n\nSchema:\n\n{\n  \"training_principles\": {\n    \"progressive_overload\": \"Detailed explanation of progressive overload methods based on scientific research\",\n    \"recovery_guidelines\": \"Evidence-based recovery protocols with optimal time frames\",\n    \"mobility_and_flexibility\": \"Research-supported mobility and flexibility practices and their integration with strength training\",\n    \"warm_up_and_cool_down\": \"Scientifically optimal warm-up and cool-down protocols with physiological justification\",\n    \"injury_prevention\": \"Research-backed strategies to minimize injury risk while maximizing training benefits\"\n  },\n  \"adjustment_guidelines\": {\n    \"plateau_breaking_strategies\": \"Scientific approaches to overcome training plateaus with physiological explanations\",\n    \"form_correction_tips\": \"Biomechanically sound technique guidelines with common error corrections\",\n    \"training_periodization\": \"Evidence-based periodization models with practical implementation details\"\n  },\n  \"performance_tracking\": {\n    \"tracking_methods\": \"Validated methods for monitoring training progress and adaptations\",\n    \"weekly_evaluation_metrics\": \"Key performance indicators backed by research on training adaptations\",\n    \"strength_progression_goals\": \"Realistic, research-supported strength development targets by training level\"\n  },\n  \"additional_recommendations_based_on_research\": [\n    {\n      \"title\": \"Title of research-based recommendation\",\n      \"description\": \"Detailed explanation of the practical recommendation\",\n      \"scientific_basis\": \"Summary of supporting research with key findings\",\n      \"implementation_strategy\": \"Step-by-step implementation protocol based on research\"\n    }\n  ]\n}",
        "temperature": 1,
        "tool_model_enabled": False,
        "top_k": None,
        "top_p": None
    },
    "TextOutput-cT1Xt": {
        "input_value": ""
    },
    "CombineText-y3nxX": {
        "delimiter": " ",
        "text1": "",
        "text2": ""
    }
    }

  try:
    result = run_flow_from_json(flow="/Users/npatel237/Athlyze/flow/Muscle.json",
                                input_value="message",
                                session_id="", # provide a session id if you want to use session state
                                fallback_to_env_vars=True, # False by default
                                tweaks=TWEAKS)

    extracted_data = result[0]
    schedule = (dict(extracted_data.outputs[0].results['text'])['data']['text'])

    result[0]
    extra = (dict(extracted_data.outputs[1].results['text'])['data']['text'])

    save_json_data(schedule, "your_training_plan.json")
    save_json_data(extra, "your_training_principles.json")

    return "Success"

  except Exception as e:
    return f"Error running the flow: {e}"
