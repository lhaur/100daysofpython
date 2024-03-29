#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

notification_manager = NotificationManager()
datamanager = DataManager()
flightsearch = FlightSearch()
sheet_data = datamanager.get_data()
ORIGIN_CITY_IATA = "HEL"
pprint(sheet_data)
for city in sheet_data:
    if not city["iataCode"]:
        iataCode = flightsearch.get_iata(city=city["city"])
        cityId = city["id"]
        datamanager.update_data(cityId=cityId, iataCode=iataCode)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flightsearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        ################
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        ################

        notification_manager.send_sms(message)