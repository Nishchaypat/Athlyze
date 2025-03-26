import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
import warnings
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG: Loading dependencies...")

try:
  from langflow.load import upload_file
except ImportError:
  warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
  upload_file = None

print("DEBUG: Dependencies loaded successfully")

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "57a0a7ce-81e6-4430-a570-5c38766b3ffd"
FLOW_ID = "9b57fdd2-9b33-4aad-94a4-2b910775aca4"
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")
ENDPOINT = "" 

goals = "Goals:  Gain: I want to gain strength and some definition in my abs and legs. I really want to get good ass and butt. Lose: I want to lose fat in my thigh region, torso region, and my upper arm region. "
notes = "Notes:  Demographic: I am a 22 year old femal. I am approximately 4'11'' and 128 lbs.  Dietary Notes: I am a pure vegetarian, my primary sources of protein are tofu, yogurt etc. Activity: I am very active I want workout for 3 days a week. I have access to limited  gym tools."

TWEAKS = {
  "GoogleGenerativeAIModel-tmINJ": {},
  "AstraDB-wHLrw": {},
  "Google Generative AI Embeddings-BZcXc": {},
  "Prompt-DQWlH": {},
  "ParseData-PBC9c": {},
  "GoogleGenerativeAIModel-EmX6l": {},
  "TextInput-E61Zz": {
    "input_value": "{notes}"
  },
  "TextInput-rZv5l": {
    "input_value": "{goals}"
  },
  "TextOutput-FoYjn": {},
  "GoogleGenerativeAIModel-ekoqV": {},
  "TextOutput-cT1Xt": {},
  "CombineText-y3nxX": {}
}

def run_flow(message: str,
  endpoint: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
  """
  Run a flow with a given message and optional tweaks.

  :param message: The message to send to the flow
  :param endpoint: The ID or the endpoint name of the flow
  :param tweaks: Optional tweaks to customize the flow
  :return: The JSON response from the flow
  """
  print(f"DEBUG: Preparing to run flow to endpoint")

  api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

  payload = {
    "input_value": message,
    "output_type": output_type,
    "input_type": input_type,
}
  if tweaks:
    payload["tweaks"] = tweaks
  if application_token:
    headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}

  print(f"DEBUG: Sending request to Langflow...")

  response = requests.post(api_url, json=payload, headers=headers)
  
  print(f"DEBUG: Received response with status code: {response.status_code}")

  if response.status_code == 200:
    print("DEBUG: Flow executed successfully")
    return response.json()
  elif response.status_code == 401:
    print("DEBUG: Authentication failed - Invalid Application Token")
    raise ValueError("Invalid Application Token")
  elif response.status_code == 404:
    print("DEBUG: Flow not found - Invalid Flow ID")
    raise ValueError("Invalid Flow ID")
  else:
    print(f"DEBUG: Unexpected error - Response: {response.text}")
    raise ValueError(f"Error running flow: {response.text}")

def save_json_data(data, filename, path="/Users/npatel237/Athlyze/backend/database"):
  print(f"DEBUG: Preparing to save data to {filename}")
  os.makedirs(path, exist_ok=True)
  
  try:
    cleaned_data = json.loads(data)
  except json.JSONDecodeError:
    print("DEBUG: Data is not a valid JSON, attempting to clean")
    cleaned_data = data.strip()
    cleaned_data = cleaned_data.replace('``````', '').strip()
    try:
      cleaned_data = json.loads(cleaned_data)
    except json.JSONDecodeError:
      print("DEBUG: Could not parse cleaned data as JSON")
      pass

  file_path = os.path.join(path, filename)
  
  with open(file_path, 'w') as f:
    json.dump(cleaned_data, f, indent=2)
  
  print(f"DEBUG: Data saved to {file_path}")


def main():
  print("DEBUG: Starting main function")
  parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
  parser.add_argument("message", type=str, help="The message to send to the flow")
  parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
  parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
  parser.add_argument("--application_token", type=str, default=APPLICATION_TOKEN, help="Application Token for authentication")
  parser.add_argument("--output_type", type=str, default="chat", help="The output type")
  parser.add_argument("--input_type", type=str, default="chat", help="The input type")
  parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)

  args = parser.parse_args()
  
  print("DEBUG: Parsing arguments")


  try:
    tweaks = json.loads(args.tweaks)
  except json.JSONDecodeError:
    print("DEBUG: Invalid tweaks JSON string")
    raise ValueError("Invalid tweaks JSON string")

  print("DEBUG: Executing run_flow")
  response = run_flow(
    message=args.message,
    endpoint=args.endpoint,
    output_type=args.output_type,
    input_type=args.input_type,
    tweaks=tweaks,
    application_token=args.application_token
  )
  
  print("DEBUG: Processing response")
  extra = (response['outputs'][0]['outputs'][1]['outputs']['text']['message'])
  save_json_data(extra, "extra_data.json")
  
  schedule = (response['outputs'][0]['outputs'][0]['outputs']['text']['message'])
  save_json_data(schedule, "schedule_data.json")

  print("DEBUG: Main function completed successfully")


if __name__ == "__main__":
  main()