from langflow.load import run_flow_from_json
import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv
import time
import json
import pandas as pd
from test_cases import TEST_CASES

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")


# Prepare results storage
results = []

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
    "input_value": ""
  },
  "TextInput-Jan01": {
    "input_value": ""
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

# Function to run test and measure performance
def run_nutrition_test(goals, notes):
    # Update TWEAKS with current test case
    TWEAKS['TextInput-Jan01']['input_value'] = goals
    TWEAKS['TextInput-pZFfT']['input_value'] = notes
    
    # Measure input size
    input_size = len(goals) + len(notes)
    
    # Time the execution
    start_time = time.time()
    
    try:
        result = run_flow_from_json(
            flow="/Users/npatel237/Athlyze/flow/Nutrition.json",
            input_value="message",
            fallback_to_env_vars=True,
            tweaks=TWEAKS
        )
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Extract data (modify based on your actual result structure)
        extracted_data = result[0]
        schedule = dict(extracted_data.outputs[0].results['text'])['data']['text']
        extra_info = dict(extracted_data.outputs[1].results['text'])['data']['text']
        
        return {
            'input_size': input_size,
            'execution_time': execution_time,
            'schedule': schedule,
            'extra_info': extra_info
        }
    
    except Exception as e:
        print(f"Error in test case: {e}")
        return None

# Run tests
for i, test_case in enumerate(TEST_CASES, 1):
    print(f"\nRunning Test Case {i}")
    
    result = run_nutrition_test(test_case['goals'], test_case['notes'])
    
    if result:
        print(f"Test Case {i} Passed - Input Size: {result['input_size']}, Execution Time: {result['execution_time']}s")
        results.append({
            'test_case_number': i,
            'input_size': result['input_size'],
            'execution_time': result['execution_time']
        })
    else:
        print(f"Test Case {i} Failed - No result returned")

# Create performance DataFrame
performance_df = pd.DataFrame(results)

# Save performance data
performance_df.to_csv('nutrition_test_performance.csv', index=False)
