import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
MY_LATITUDE = YOUR_LAT
MY_LONGITUDE = YOUR_LON
CNT = 4
UNITS = "metric"

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
my_phone_num = os.getenv("PHONE_NUM")


PARAMETERS = {"lat": MY_LATITUDE,
              "lon": MY_LONGITUDE,
              "appid": API_KEY,
              "cnt": CNT,
              "units": UNITS
}
URL = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(URL, params=PARAMETERS)
response.raise_for_status()

weather_data = response.json()
print(weather_data)

weather_ids = [weather_data["list"][list_n]["weather"][0]["id"] for list_n in range(4)]
#print(weather_ids)

will_rain = [weather_id for weather_id in weather_ids if weather_id < 700]
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain. Grab an umbrella",
        from_="TWILIO_NUMBER",
        to=my_phone_num
    )

    print(message.status)

