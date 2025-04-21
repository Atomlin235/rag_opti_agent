
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


secret = st.secrets["APP_TOKEN"]

def run_flow(message:str) -> dict:
# The complete API endpoint URL for this flow
    url = f"https://api.langflow.astra.datastax.com/lf/9a7c0926-9871-4088-aa00-ebc443634b9e/api/v1/run/6a9ffb4a-bca0-4f80-a3ee-7bc0b8665874"  

# Request payload configuration
    payload = {
        "input_value": message,  # The input value to be processed by the flow
        "output_type": "chat",  # Specifies the expected output format
        "input_type": "chat"  # Specifies the input format
    }

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization":f"Bearer {secret}"  # Authentication key from environment variable'}
    }

    try:
        # Send API request
        response = requests.request("POST", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        # Print response
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except ValueError as e:
        print(f"Error parsing response: {e}")


def main():
    st.title("Strategy Interface")

    message = st.text_area("Message", placeholder="Input Opti Details And Ask A Question")

    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
        
        try:
            with st.spinner("Running Flow"):
                response = run_flow(message)
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
