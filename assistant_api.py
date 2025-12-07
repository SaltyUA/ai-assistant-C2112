import requests
import json

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \

headers = {     
    "Content-Type": "application/json",
    "X-goog-api-key": "AIzaSyAkxYL_6NdIEmpy-dv51oqB-j0JgW9phnc"
    }

payload = {
    "contents": [
        {
        "parts": [
            {
            "text": "Explain how AI works in a few words"
            }
        ]
        }
    ]
}


response = requests.post(URL, headers=headers, json=payload)
print(response.json())