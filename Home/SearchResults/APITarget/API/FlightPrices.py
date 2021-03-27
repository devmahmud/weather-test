import requests
from amadeus import Client, ResponseError
import json


class FlightPrices:
    def __init__(self, origin, destination, date, num_adults):
        self.client = Client(
            client_id='sz2uYf85WPgWWej1LZzAOCcToZcmTheX',
            client_secret='ZZZkKyLn3XK6vqji'
        )

        self.origin = origin
        self.destination = destination
        self.date = date
        self.num_adults = num_adults

        self.data = None

    def getData(self):
        try:
            response = self.client.shopping.flight_offers_search.get(originLocationCode=f'{self.origin}',
                                                                     destinationLocationCode=f'{self.destination}',
                                                                     departureDate=f'{self.date}',
                                                                     adults=self.num_adults)
        except ResponseError as error:
            raise error

        self.data = response.data

    def modifyData(self):
        modified_data = self.data
        modified_data = json.dumps(modified_data, indent=4)
        #
        # Make modifications here
        #
        #print(modified_data)
        self.data = modified_data


if __name__ == "__main__":
    api = FlightPrices('MAN', 'OPO', '2021-05-27', 1)
    api.getData()
    api.modifyData()
