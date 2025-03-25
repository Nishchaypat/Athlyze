import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
import warnings
import os
from dotenv import load_dotenv

load_dotenv()

try:
    from langflow.load import upload_file
except ImportError:
    warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
    upload_file = None

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "57a0a7ce-81e6-4430-a570-5c38766b3ffd"
FLOW_ID = "9b57fdd2-9b33-4aad-94a4-2b910775aca4"
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")
ENDPOINT = "" 


TWEAKS = {
  "GoogleGenerativeAIModel-tmINJ": {},
  "AstraDB-wHLrw": {},
  "Google Generative AI Embeddings-BZcXc": {},
  "Prompt-DQWlH": {},
  "ParseData-PBC9c": {},
  "GoogleGenerativeAIModel-EmX6l": {},
  "TextInput-E61Zz": {},
  "TextInput-rZv5l": {},
  "TextOutput-FoYjn": {},
  "TextInput-0qayZ": {},
  "GoogleGenerativeAIModel-ekoqV": {},
  "TextOutput-cT1Xt": {}
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

    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise ValueError("Invalid Application Token")
    elif response.status_code == 404:
        raise ValueError("Invalid Flow ID")
    else:
        raise ValueError(f"Error running flow: {response.text}")

def main():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("message", type=str, help="The message to send to the flow")
    parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
    parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
    parser.add_argument("--application_token", type=str, default=APPLICATION_TOKEN, help="Application Token for authentication")
    parser.add_argument("--output_type", type=str, default="chat", help="The output type")
    parser.add_argument("--input_type", type=str, default="chat", help="The input type")
    parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)

    args = parser.parse_args()
    try:
      tweaks = json.loads(args.tweaks)
    except json.JSONDecodeError:
      raise ValueError("Invalid tweaks JSON string")

    response = run_flow(
        message=args.message,
        endpoint=args.endpoint,
        output_type=args.output_type,
        input_type=args.input_type,
        tweaks=tweaks,
        application_token=args.application_token
    )
    schedule = (response['outputs'][0]['outputs'][0]['outputs']['text']['message'])
    print(json.dumps(schedule, indent=2))
    print("\n\n")
    extra = (response['outputs'][0]['outputs'][1]['outputs']['text']['message'])
    print(json.dumps(extra, indent=2))
    #print(json.dumps(response, indent=2))

if __name__ == "__main__":
    main()
