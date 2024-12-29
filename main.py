# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "baf5b460-1478-4a11-90c7-84a4ea5036c6"
FLOW_ID = "0ccc02d1-e1bc-4350-9770-00d7793b9dcf"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "" # The endpoint name of the flow


def run_flow(message: str) -> dict:
   
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
  
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    message = st.text_area("Enter your message", placeholder="Ask something ...")

    if st.button("Runflow"):
        if not message.strip():
            st.warning("Please enter a message")
            return
        try:
            with st.spinner("Running flow ..."):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(f"An error occurred: {e} {response}")

if __name__ == "__main__":
    main()
