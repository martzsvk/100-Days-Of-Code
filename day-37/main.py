import requests
import datetime
import os
from dotenv import load_dotenv
from app import App


load_dotenv()

# Constants
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

# Creating User
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# USER_PARAMS = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)

# Creating Graph
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/USER/graphs"

# GRAPH_PARAMS = {
#     "id": GRAPH_ID,
#     "name": "Programming",
#     "unit": "minutes",
#     "type": "int",
#     "color": "momiji",
#
# }

HEADERS = {
     "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=HEADERS)
# print(response.text)

# Update graph
UPDATE_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

# UPDATE_PARAMS = {
#     "color": "momiji",
#     "timezone": "CET",
#     "startOnMonday": True
# }

# update = requests.put(url=UPDATE_ENDPOINT, json=UPDATE_PARAMS, headers=HEADERS)
# print(update.text)

# Posting a pixel
# POST_PIXEL_ENDPOINT is the same as UPDATE_ENDPOINT

def handle_submit(time_programming):
    date = datetime.datetime.now().strftime("%Y%m%d")

    PIXEL_PARAMS = {
        "date": date,
        "quantity": time_programming
    }

    response = requests.post(url=UPDATE_ENDPOINT, json=PIXEL_PARAMS, headers=HEADERS)
    print(response.text)

app = App(handle_submit)
app.mainloop()

# Updating pixel
# UPDATE_PIXEL_END = f"{UPDATE_ENDPOINT}/{date}"
#
# UPDATE_PIXEL_PARAMS = {
#     "quantity": "80"
# }

# response = requests.put(url=UPDATE_PIXEL_END, json=UPDATE_PIXEL_PARAMS, headers=HEADERS)
# print(response.text)


# Deleting pixel
# DELETING_ENDPOINT is the same as a UPDATE_PIXEL_END

# response = requests.delete(url=UPDATE_PIXEL_END, headers=HEADERS)
# print(response.text)
