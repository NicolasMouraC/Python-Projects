import os
import datetime as dt
import requests
from pprint import pprint

date = dt.datetime.now()

class FlightSearch:
    '''Makes a request to the kiwi api and then format the userful data into a dictionary'''

    def flight_search(self, data_class):
        tequila_endpoint = os.environ.get("TEQUILA_ENDPOINT")
        tequila_header = {"apiKey": os.environ.get("TEQUILA_KEY"),
                          "Content_Type": "application/json"}
        today = date.strftime("%d/%m/%Y")
        six_months = date.strftime("%d/12/%Y")

        flights_dict = []

        for item in range(len(data_class)):
            tequila_parameters = {"fly_from": "SAO",
                                  "fly_to": data_class[item]["iataCode"],
                                  "price_to": data_class[item]["lowestPrice"],
                                  "date_from": today,
                                  "date_to": six_months,
                                  "max_stopovers" : 0,
                                  "curr": "BRL"}
            print(data_class[item]["iataCode"])
            print(data_class[item]["lowestPrice"])
            request = requests.get(url=tequila_endpoint, headers=tequila_header, params=tequila_parameters)
            try:
                data = request.json()["data"]
            except KeyError:
                pass
            else:
                try:
                    flights_dict.append({
                        "fly_from": data[item - 1]["flyFrom"],
                        "city_from": data[item - 1]["cityFrom"],
                        "fly_to": data[item - 1]["flyTo"],
                        "city_to": data[item - 1]["cityTo"],
                        "price": data[item - 1]["price"],
                        "local_departure": data[item - 1]["local_departure"],
                        "return_date": data[item]["local_departure"],
                        "stop_over": 0
                        })
                except IndexError:
                    try:
                        tequila_parameters["max_stopovers"] = 1
                        request = requests.get(url=tequila_endpoint, headers=tequila_header, params=tequila_parameters)
                        data = request.json()["data"]
                        flights_dict.append({"fly_from": data[item - 1]["flyFrom"],
                                            "city_from": data[item - 1]["cityFrom"],
                                            "fly_to": data[item - 1]["flyTo"],
                                            "city_to": data[item - 1]["cityTo"],
                                            "price": data[item - 1]["price"],
                                            "local_departure": data[item - 1]["local_departure"],
                                            "return_date": data[item]["local_departure"],
                                            "stop_over": 1
                                        })
                    except:
                        pass

        return flights_dict
