from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Initializing classes
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()

# Checking if row with IATA codes is empty
for row in sheet_data:
    if row["iataCode"] == "":
        # Putting the name of the city where the IATA code is missing
        iata_code = flight_search.get_iata_code(city_name=row["city"])
        row["iataCode"] = iata_code
        # Putting IATA code into Google Sheet
        data_manager.update_iata_code(row_id=row["id"], iata_code=iata_code)


for row in sheet_data:
    flight_data = flight_search.search_flights(row["iataCode"])
    cheapest_flight = flight_search.find_cheapest_flight(flight_data)

    if cheapest_flight:
        notification_manager.send_message(cheapest_flight)
    else:
        print(f"{row['city']}: no flights found.")





