import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ✅ CORRECT: Get the API key from environment variable
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json"
}

def call_llm(prompt):
    if not NVIDIA_API_KEY:
        return "ERROR: NVIDIA_API_KEY is not set. Please check your .env file."
    
    payload = {
        "model": "meta/llama3-8b-instruct",
        "messages": [
            {"role": "system", "content": "You are a compassionate, experienced doctor who explains medical information clearly and kindly to patients. You use simple language, avoid unnecessary jargon, and format your responses with clear sections and bullet points for easy reading."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1000
    }

    response = requests.post(NVIDIA_URL, headers=HEADERS, json=payload)

    # ❌ HTTP-level error
    if response.status_code != 200:
        return f"NVIDIA HTTP Error {response.status_code}: {response.text}"

    try:
        data = response.json()
    except json.JSONDecodeError:
        return f"Invalid JSON from NVIDIA: {response.text}"

    # ❌ NVIDIA API error response
    if "error" in data:
        return f"NVIDIA API Error: {data['error']}"

    # ❌ Missing expected output
    if "choices" not in data:
        return f"Unexpected NVIDIA response format: {data}"

    return data["choices"][0]["message"]["content"]
