import requests
from datetime import datetime
import smtplib
import time

# Constants
MY_LAT = YOUR_LAT
MY_LNG = YOUR_LNG
MY_EMAIL = "YOUR_MAIL"
PASSWORD = "YOUR_PASSWORD"

def iss_position():
    # ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    if MY_LAT == iss_lat and MY_LNG == iss_lng:
        return True
    else:
        return False


def is_night():
    # Parameters for API Sunrise-Sunset
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    # Sunrise-Sunset API
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if sunrise > hour > sunset:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if iss_position() and is_night():
        # Sending email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: ISS is at your city \n\n Look up")


