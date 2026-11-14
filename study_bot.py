import os 
import requests


from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")


print(len(api_key)) 


url ="https://generativelanguage.googleapis.com/v1beta/interactions"

headers =  {
    "x-goog-api-key": api_key,
    "Content-Type": "application/json",
}



body = {
    "model": "gemini-3.6-flash",
    "input": input("enter ur quistion")
  }

response = requests.post(url, headers=headers, json=body)

print(response.status_code)
print(response.json())
