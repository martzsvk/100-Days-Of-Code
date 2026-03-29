import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData


load_dotenv()


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


class FlightSearch:

    def get_token(self):
        url_token = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }

        response = requests.post(url=url_token, data=data, headers=headers)
        return response.json()["access_token"]


    def get_iata_code(self, city_name):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        bearer = self.get_token()

        amadeus_params = {
            "keyword": city_name
        }

        headers = {
            "Authorization": f"Bearer {bearer}"
        }

        try:
            response = requests.get(url=url, params=amadeus_params, headers=headers)
            response = response.json()
            return response["data"][0]["iataCode"]
        except KeyError:
            return f"None for {city_name}"

    def search_flights(self, destination_code):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        bearer = self.get_token()
        headers = {
            "Authorization": f"Bearer {bearer}"
        }

        departure_date = datetime.now() + timedelta(days=1)
        departure_date = departure_date.strftime("%Y-%m-%d")
        return_date = datetime.now() + timedelta(days=180)
        return_date = return_date.strftime("%Y-%m-%d")

        params = {
            "originLocationCode": "VIE",
            "destinationLocationCode": destination_code,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "currencyCode": "EUR",
            "nonStop": "false"
        }

        try:
            response = requests.get(url=url, params=params, headers=headers)
            return response.json()
        except KeyError:
            return None


    def find_cheapest_flight(self, data):
        if data is None or not data.get("data"):
            return None

        cheapest_price = float("inf")
        cheapest_flight = None

        for flight in data["data"]:
            price = float(flight["price"]["grandTotal"])

            if price < cheapest_price:
                cheapest_price = price

                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

                cheapest_flight = FlightData(
                    price=price,
                    origin_city=flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                    origin_airport=flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                    destination_city=flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                    destination_airport=flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                    out_date=out_date,
                    return_date=return_date
                )

        return cheapest_flight











