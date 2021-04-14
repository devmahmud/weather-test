import requests
import json


class AirPollution:
    def __init__(self, lat, long):  # Declare all variables that will be needed for this api (url, country code, etc...)

        self.url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid=734c78c5952649e67d970148d082c284"
        self.data = None
        self.items = []

    def getData(self):  # Method used to get a response from the APITarget
        response = requests.get(self.url)
        self.data = response.json()

    def modifyData(self):  # Method used to modify the json data to provide only the data that is needed
        modified_data = self.data

        modified_data = json.dumps(modified_data, indent=4)

        self.data = modified_data
        print(self.data)


if __name__ == "__main__":
    api = AirPollution(25, 75)
    api.getData()
    api.modifyData()
