import os 
import requests
import time


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
    "input": input("enter your quistion: ")
  }

attempts = 0

while attempts < 3:
    attempts +=1

    response = requests.post(url, headers=headers, json=body)

    status = response.status_code

    print(f"tries: {attempts}, status: {status}")

    if status == 200:

      data = response.json()

      answer = data["steps"][1]["content"][0]["text"]

      print(answer)
      break
    elif status == 429 or status >= 500:
       time.sleep(3)
    else:
       print("The problem is on the user side")
       break
print("Thank You")       
