import requests

# Parameters for API request
parameters = {
    "amount": 10,
    "category": 23,
    "difficulty": "medium",
    "type": "boolean"
}

# API request
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
# JSON data
data = response.json()
question_data = data["results"]



