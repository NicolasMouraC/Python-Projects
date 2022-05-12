import os
import requests


class DataManager:
    '''Gets data through a Google sheet api request'''

    def get_data(self):
        request = requests.get(url=os.environ.get("SHEETY_API"))
        self.data = request.json()["prices"]
        return self.data
