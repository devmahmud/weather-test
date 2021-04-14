import requests
import json


class FloodWarnings:
    def __init__(self):  # Declare all variables that will be needed for this api (url, country code, etc...)
        self.url = "https://environment.data.gov.uk/flood-monitoring/id/floods?min-severity=3"
        self.data = None
        self.items = []

    def getData(self):  # Method used to get a response from the APITarget
        response = requests.get("https://environment.data.gov.uk/flood-monitoring/id/floods?min-severity=3")
        self.data = response.json()

    def modifyData(self):  # Method used to modify the json data to provide only the data that is needed
        modified_data = self.data
        print(modified_data)

        modified_data.pop('@context', None)  # Removes context element
        modified_data.pop('meta', None)  # Removes meta element

        self.data = json.dumps(modified_data, indent=4)  # Should only contain items element

        print(self.data)


if __name__ == "__main__":
    api = FloodWarnings()
    api.getData()
    api.modifyData()
