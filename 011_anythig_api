import os

import requests
from dotenv import load_dotenv

load_dotenv(override=True)

# api_key
# api_key = "your_api_key"
api_key = os.getenv("ANYTHING_LLM_API_KEY")

message = "your message"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

json_data = {
    "message": message,
    "mode": "query",
}

response = requests.post(
    "http://localhost:3001/api/v1/workspace/aiden-ws/chat",
    headers=headers,
    json=json_data,
)

# 결과 파싱
rlt_json = response.json()
text_res = rlt_json["textResponse"]
print(text_res)