from langflow.load import run_flow_from_json
import os
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

def save_json_data(data, filename, path="database/"):
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
    "GoogleGenerativeAIModel-RmN9Z": {
    "api_key": GEMINI_API_KEY,
    "input_value": "",
    "max_output_tokens": None,
    "model_name": "gemini-1.5-flash-latest",
    "n": None,
    "stream": False,
    "system_message": "Convert the provided user information into at least five diverse and precise search queries for retrieving relevant muscle training research papers vector database. Ensure the queries cover different aspects such as training techniques, recovery methods, injury prevention, progressive overload ensuring muscle growth. Return only the generated text queries in a single paragraph, separated by periods, without any additional text or explanations.",
    "temperature": 0.1,
    "tool_model_enabled": False,
    "top_k": None,
    "top_p": None
    },
    "AstraDB-Gahxt": {
    "advanced_search_filter": "{}",
    "api_endpoint": "https://15e39959-c28e-49d1-bde1-a8af867e42d4-us-east1.apps.astra.datastax.com",
    "astradb_vectorstore_kwargs": "{}",
    "autodetect_collection": True,
    "collection_name": "nutrition_research_collection",
    "content_field": "",
    "database_name": "nutrition_research_papers",
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
    "Google Generative AI Embeddings-o7dcw": {
    "api_key": GEMINI_API_KEY,
    "model_name": "models/text-embedding-004"
    },
    "Prompt-wO4NQ": {
    "template": "You are an expert fitness trainer specializing in evidence-based nutrition planner. Using the scientific research provided below, create a comprehensive, personalized nutrition plan that fits User Profile and the research data\n\nRESEARCH DATABASE:\n{nutrition_data}\n\nUSER PROFILE:\n- Notes: {notes}\n- Goals: {goals}\n\nINSTRUCTIONS:\n1. Analyze the user's notes and goals to create a fully personalized plan\n2. Base all recommendations on scientific evidence from the provided research\n3. Include clear explanations for why each nutrition recommendation was selected\n4. Provide detailed instructions for proper exercise technique\n5. Design a progressive plan that adapts over time as the user advances\n6. Include strategies for tracking progress and making adjustments when needed\n7. Consider any health conditions or limitations mentioned in the user notes\n\nYour response should be comprehensive, scientifically sound, and practical for implementation.\n\nVery Important: Make sure to return the response without any ```json```.",
    "tool_placeholder": "",
    "notes": "",
    "goals": "",
    "nutrition_data": ""
    },
    "ParseData-1vCgo": {
    "sep": "\n",
    "template": "{text}"
    },
    "GoogleGenerativeAIModel-dv0MW": {
    "api_key": GEMINI_API_KEY,
    "input_value": "",
    "max_output_tokens": 40000000,
    "model_name": "gemini-2.0-flash-thinking-exp-01-21",
    "n": None,
    "stream": False,
    "system_message": "You are an advanced AI assistant specializing in creating scientifically-backed nutrition plans. Your task is to generate a comprehensive Diet Plan in JSON format, tailored to the user's specific details provided below. Each recommendation must be supported by scientific evidence. Ensure the output strictly matches the provided JSON schema and fits within the typical token limits of AI responses.\n\nVery Important: Make sure to return the response without any ```json```.\n\nSchema:\n\n{\n  \"intro\": \"Brief introduction summarizing the objectives and scope of the diet plan.\",\n  \"diet_schedule\": {\n    \"caloric_needs\": {\n      \"daily_calories\": \"\",\n      \"calculation_method\": \"\",\n      \"adjustment_factors\": \"\"\n    },\n    \"macronutrient_distribution\": {\n      \"protein\": \"\",\n      \"carbohydrates\": \"\",\n      \"fats\": \"\",\n      \"explanation\": \"\"\n    },\n    \"daily_meal_plan\": {\n      \"Monday\": {\n        \"breakfast\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"lunch\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"pre_workout\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"dinner\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        }\n      },\n      \"Tuesday\": {\n        \"breakfast\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"lunch\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"pre_workout\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"dinner\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        }\n      },\n      \"Wednesday\": {\n        \"breakfast\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"lunch\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"pre_workout\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"dinner\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        }\n      },\n      \"Thursday\": {\n        \"breakfast\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"lunch\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"pre_workout\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"dinner\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        }\n      },\n      \"Friday\": {\n        \"breakfast\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"lunch\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"pre_workout\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"dinner\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        }\n      },\n      \"Saturday\": {\n        \"breakfast\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"lunch\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"pre_workout\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"dinner\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        }\n      },\n      \"Sunday\": {\n        \"breakfast\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"lunch\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"pre_workout\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        },\n        \"dinner\": {\n          \"name\": \"\",\n          \"calories\": \"\",\n          \"macros\": {\n            \"protein\": \"\",\n            \"carbs\": \"\",\n            \"fats\": \"\"\n          },\n          \"ingredients\": [],\n          \"alternatives\": []\n        }\n      }\n    }\n    }\n  }\n\n",
    "temperature": 0.8,
    "tool_model_enabled": False,
    "top_k": None,
    "top_p": None
    },
    "TextInput-pZFfT": {
    "input_value": notes
    },
    "TextInput-Jan01": {
    "input_value": goals
    },
    "TextOutput-BOXES": {
    "input_value": ""
    },
    "GoogleGenerativeAIModel-hP3bM": {
    "api_key": GEMINI_API_KEY,
    "input_value": "",
    "max_output_tokens": 4000000,
    "model_name": "learnlm-1.5-pro-experimental",
    "n": None,
    "stream": False,
    "system_message": "You are an advanced AI assistant specializing in creating scientifically-backed nutrition plans. Your task is to generate a comprehensive Diet Plan in JSON format, tailored to the user's specific details provided below. Ensure the output strictly matches the provided JSON schema and fits within the typical token limits of AI responses.\n\nVery Important: Make sure to return the response without any ```json```.\n\nSchema:\n\n{\n    \"hydration_guidelines\": {\n      \"daily_water_intake\": \"\",\n      \"timing_strategy\": \"\",\n      \"explanation\": \"\"\n    },\n      \"adjustment_guidelines\": {\n        \"weight_loss_plateau\": \"\",\n        \"strength_plateau\": \"\",\n        \"energy_issues\": \"\"\n     },\n    \"additional_recommendations_based_on_research\": [\n      {\n        \"title\": \"\",\n        \"description\": \"\",\n        \"scientific_basis\": \"\",\n        \"implementation_strategy\": \"\"\n      }\n    ]\n}",
    "temperature": 0.8,
    "tool_model_enabled": False,
    "top_k": None,
    "top_p": None
    },
    "TextOutput-FxfEB": {
    "input_value": ""
    },
    "CombineText-PzQ7O": {
    "delimiter": " ",
    "text1": "",
    "text2": ""
    }
  }
  try:
    result = run_flow_from_json(flow="flow/Nutrition.json",
                                input_value="message",
                                session_id="", # provide a session id if you want to use session state
                                fallback_to_env_vars=True, # False by default
                                tweaks=TWEAKS)

    extracted_data = result[0]
    schedule = (dict(extracted_data.outputs[0].results['text'])['data']['text'])

    result[0]
    extra = (dict(extracted_data.outputs[1].results['text'])['data']['text'])

    save_json_data(schedule, "your_nutrition_plan.json")
    save_json_data(extra, "your_nutrition_principles.json")

    return "Success"

  except Exception as e:
    return f"Error running the flow: {e}"
