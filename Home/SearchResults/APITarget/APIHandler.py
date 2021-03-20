import json
import time
import argparse

from .API.FloodWarnings import FloodWarnings
from .API.CurrentWeather import CurrentWeather
from .API.AirPollution import AirPollution
from .API.FlightPrices import FlightPrices


class APIHandler:
    def __init__(self, api="FloodWarnings", latitude=0, longitude=0, origin="BHX", destination="PAR", date="2021-03-26",
                 num_adults=1):
        self.api_list = {
            "FloodWarnings": "https://environment.data.gov.uk/flood-monitoring/id/floods?min-severity=3",
            # Lists all flood warnings in UK
            "CurrentWeather": "api.openweathermap.org/data/2.5/weather?",  # Choose  city name
            "FlightPrices": "https://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/",
            # Requires Origin Airport Code, Destination Airport Code, Outbound Date, Number of Adults
            "AirPollution": "http://api.openweathermap.org/data/2.5/air_pollution?",
            # Requires latitude and longitude coords
        }

        self.requested_API = api
        self.latitude = latitude
        self.longitude = longitude
        self.origin = origin
        self.destination = destination
        self.date = date
        self.num_adults = num_adults

        self.get_data()

        self.data = None

    def get_data(self):  # Method to contain the calls to different classes in the APITarget folder
        if self.requested_API in self.api_list:
            if self.requested_API == "FloodWarnings":
                api = FloodWarnings()
                api.getData()
                api.modifyData()
                self.data = api.data
                pass  # Placeholder
            elif self.requested_API == "CurrentWeather":
                api = CurrentWeather(self.latitude, self.longitude)
                api.getData()
                api.modifyData()
                self.data = api.data
                pass  # Placeholder
            elif self.requested_API == "AirPollution":
                api = AirPollution(self.latitude, self.longitude)
                api.getData()
                api.modifyData()
                self.data = api.data
                pass  # Placeholder
            elif self.requested_API == "FlightPrices":
                api = FlightPrices(self.origin, self.destination, self.date, self.num_adults)
                api.getData()
                api.modifyData()
                self.data = api.data
        else:
            raise Exception("APITarget doesn't exist")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Placeholder to demonstrate what inputs should be provided')
    parser.add_argument('--api', type=str, default="FloodWarnings", help="APITarget to be accessed")
    parser.add_argument('--city_name', type=str, default="Coventry", help="String of city name")
    parser.add_argument('--lat', type=int, default=0, help="Select Latitude for Air Pollution")
    parser.add_argument('--long', type=int, default=0, help="Select Longitude for Air Pollution")
    parser.add_argument('--origin', type=str, default='BHX', help="Airport code for origin in FLightPrices")
    parser.add_argument('--destination', type=str, default='BHX', help="Airport code for destination")
    parser.add_argument('--date', type=str, default='2021-12-31', help="Select flight date")
    parser.add_argument('--num_adults', type=int, default=1, help="Number of adults travelling")

    # To access the FloodWarnings Data = python APIHandler.py --api FloodWarnings
    # To access the CurrentWeather = python APIHandler.py --api CurrentWeather
    # To access the AirPollution = python APIHandler.py --api AirPollution --lat 0 --long 0
    # To access the FlightPrices = python APIHandler.py --api FlightPrices --origin BHX --destination PAR --date 2021-12-31 --num_adults 1

    args = parser.parse_args()
    APIHandler()
