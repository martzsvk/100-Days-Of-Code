import os
from dotenv import load_dotenv
from twilio.rest import Client
from flight_data import FlightData


load_dotenv()


account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
phone_num = os.getenv("MY_PHONE_NUM")

class NotificationManager:

    def send_message(self, flight: FlightData):
        client = Client(account_sid,auth_token)

        client.messages.create(
            body=f"{flight.destination_city}\n"
                f"From {flight.origin_airport} to {flight.destination_airport}\n"
                f"Flight price: {flight.price}\n"
                f"Out on {flight.out_date} return in {flight.return_date}",
            from_="TWILIO_NUMBER",
            to=f"{phone_num}"
        )







