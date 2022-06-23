import os
import requests


class DataManager:
    '''Gets data through a Google sheet api request'''

    def get_data(self):
        request = requests.get(url='https://api.sheety.co/c0a871fe29358068d2074551e0b27f5a/flightdeals/prices') #os.environ.get('Sheety_endpoint'))
        self.data = request.json()["prices"]
        return self.data
