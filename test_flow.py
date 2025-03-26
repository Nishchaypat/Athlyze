import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
import warnings
import os
import time
import logging
from dotenv import load_dotenv

try:
  from langflow.load import upload_file
except ImportError:
  warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
  upload_file = None

# Configure logging
logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s',
  handlers=[
    logging.FileHandler("langflow_script.log"),
    logging.StreamHandler()
  ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configuration Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "57a0a7ce-81e6-4430-a570-5c38766b3ffd"
FLOW_ID = "9b57fdd2-9b33-4aad-94a4-2b910775aca4"
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")
ENDPOINT = ""

# Default goals and notes (with placeholders)
goals = "Goals:  Gain: I want to gain strength and some definition in my abs and legs. I really want to get good ass and butt. Lose: I want to lose fat in my thigh region, torso region, and my upper arm region. "
notes = "Notes:  Demographic: I am a 22 year old female. I am approximately 4'11'' and 128 lbs.  Dietary Notes: I am a pure vegetarian, my primary sources of protein are tofu, yogurt etc. Activity: I am very active I want workout for 3 days a week. I have access to limited gym tools."

# Tweaks configuration (with formatting for placeholders)
TWEAKS = {
  "TextInput-E61Zz": {
    "input_value": notes
  },
  "TextInput-rZv5l": {
    "input_value": goals
  },
  # Other tweaks remain the same
}

def run_flow_with_retries(
  message: str,
  endpoint: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None,
  max_retries: int = 3,
  initial_wait: float = 1.0
) -> dict:
  """
  Run a flow with robust error handling and retry mechanism.

  :param message: The message to send to the flow
  :param endpoint: The ID or the endpoint name of the flow
  :param max_retries: Maximum number of retry attempts
  :param initial_wait: Initial wait time between retries (exponential backoff)
  :return: The JSON response from the flow
  """
  api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

  for attempt in range(max_retries):
      try:
          payload = {
              "input_value": message,
              "output_type": output_type,
              "input_type": input_type,
          }
          
          if tweaks:
              payload["tweaks"] = tweaks
          
          headers = {
              "Authorization": f"Bearer {application_token}",
              "Content-Type": "application/json"
          }

          logger.info(f"Attempt {attempt + 1}: Sending request to Langflow...")

          response = requests.post(
              api_url, 
              json=payload, 
              headers=headers, 
              timeout=30  # Added timeout to prevent hanging
          )

          logger.info(f"Response status code: {response.status_code}")

          # Successful response
          if response.status_code == 200:
              logger.info("Flow executed successfully")
              return response.json()
          
          # Authentication failure
          elif response.status_code == 401:
              logger.error("Authentication failed - Invalid Application Token")
              raise ValueError("Invalid Application Token")
          
          # Flow not found
          elif response.status_code == 404:
              logger.error("Flow not found - Invalid Flow ID")
              raise ValueError("Invalid Flow ID")
          
          # Timeout or server issues - retry
          elif response.status_code in [504, 502, 503, 500]:
              wait_time = initial_wait * (2 ** attempt)
              logger.warning(f"Retryable error. Waiting {wait_time} seconds...")
              time.sleep(wait_time)
              continue
          
          # Unexpected error
          else:
              logger.error(f"Unexpected error: {response.text}")
              raise ValueError(f"Error running flow: {response.text}")

      except requests.exceptions.RequestException as e:
          logger.error(f"Network error on attempt {attempt + 1}: {e}")
          
          # If it's the last attempt, re-raise the exception
          if attempt == max_retries - 1:
              raise

          # Wait before next retry
          wait_time = initial_wait * (2 ** attempt)
          logger.warning(f"Network error. Waiting {wait_time} seconds...")
          time.sleep(wait_time)

  # If all retries fail
  raise RuntimeError("Failed to execute flow after maximum retries")

def save_json_data(data, filename, path="/Users/npatel237/Athlyze/backend/database"):
  """
  Save JSON data with robust error handling and logging
  """
  try:
      os.makedirs(path, exist_ok=True)
      file_path = os.path.join(path, filename)

      # Attempt to parse and clean the data
      if isinstance(data, str):
          data = data.strip().replace('``````', '').strip()
      
      try:
          parsed_data = json.loads(data) if isinstance(data, str) else data
      except json.JSONDecodeError:
          logger.warning("Could not parse data as JSON. Saving as-is.")
          parsed_data = data

      with open(file_path, 'w') as f:
          json.dump(parsed_data, f, indent=2)
      
      logger.info(f"Data saved to {file_path}")
  
  except Exception as e:
      logger.error(f"Error saving JSON data: {e}")
      raise

def main():
  logger.info("Starting main function")
  
  parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
  parser.add_argument("message", type=str, help="The message to send to the flow")
  parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
  parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
  parser.add_argument("--application_token", type=str, default=APPLICATION_TOKEN, help="Application Token for authentication")
  parser.add_argument("--output_type", type=str, default="chat", help="The output type")
  parser.add_argument("--input_type", type=str, default="chat", help="The input type")
  parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)

  args = parser.parse_args()
  
  logger.info("Parsing arguments")

  try:
      tweaks = json.loads(args.tweaks)
  except json.JSONDecodeError:
      logger.error("Invalid tweaks JSON string")
      raise ValueError("Invalid tweaks JSON string")

  try:
      logger.info("Executing run_flow")
      response = run_flow_with_retries(
          message=args.message,
          endpoint=args.endpoint,
          output_type=args.output_type,
          input_type=args.input_type,
          tweaks=tweaks,
          application_token=args.application_token
      )
      
      logger.info("Processing response")
      extra = response['outputs'][0]['outputs'][1]['outputs']['text']['message']
      save_json_data(extra, "training_principle.json")
      
      schedule = response['outputs'][0]['outputs'][0]['outputs']['text']['message']
      save_json_data(schedule, "training_schedule.json")

      logger.info("Main function completed successfully")

  except Exception as e:
      logger.error(f"Execution failed: {e}")
      raise

if __name__ == "__main__":
  main()