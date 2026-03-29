import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "YOUR_SHEET"

BEARER = os.getenv("BEARER")
headers = {
    "Authorization": f"Bearer {BEARER}"
}


class DataManager:

    def get_data(self):
        response = requests.get(url=url, headers=headers)
        data = response.json()

        return data["YOUR_SHEET_NUM"]


    def update_iata_code(self, row_id, iata_code):
        url_put = f"YOUR_SHEET"

        data = {
            "YOUR_SHEET_NUM": {
                "iataCode": iata_code
            }
        }

        response = requests.put(url=url_put, json=data, headers=headers)
        print(response.text)




