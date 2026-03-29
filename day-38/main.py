import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Nutrition API's part
APP_KEY = os.getenv("APP_KEY")
APP_ID = os.getenv("APP_ID")

app_params = {
    "query": input("Which exercises did you do? ")
}

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

response_exercise = requests.post(url=url, json=app_params, headers=headers)
response_exercise = response_exercise.json()

exercise = response_exercise["exercises"][0]["name"]
duration = response_exercise["exercises"][0]["duration_min"]
calories = response_exercise["exercises"][0]["nf_calories"]


# Sheet's part
TOKEN = os.getenv("TOKEN")
sheet_url = "YOUR_SHEET"

today = datetime.datetime.now()
today_date = today.strftime("%d.%m.%Y")
time = today.strftime("%H:%M:%S")

BEARER = os.getenv("BEARER")

bearer_headers = {
    "Authorization": f"Bearer {BEARER}"
}

sheet_params = {
    "YOUR_SHEET_NUMBER": {
        "date": today_date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

response_sheet = requests.post(url=sheet_url, json=sheet_params, headers=bearer_headers)
print(response_sheet.text)




