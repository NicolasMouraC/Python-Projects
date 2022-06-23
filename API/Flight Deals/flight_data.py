# coding=utf8

class FlightData:
    '''Formats the dictionary information into a message to be sent'''

    def organize_sms(self, dictionary : dict):
        messages = []
        for i in range(len(dictionary)):
            messages.append(f'''Low price alert! Only R${dictionary[i]['price']}\n
To fly from {dictionary[i]['city_from']}-{dictionary[i]['fly_from']} to {dictionary[i]['city_to']}-{dictionary[i]['fly_to']}\n
Departure date: {dictionary[i]["local_departure"]}\n
Return date: {dictionary[i]["return_date"]}\n
Stop Over: {dictionary[i]["stop_over"]}
Here is a link to the for the flight: 
https://www.google.com.br/flights?hl=en#flt={dictionary[i]["fly_from"]}.{dictionary[i]["fly_to"]}.{dictionary[i]["local_departure"].split("T")[0]}*{dictionary[i]["fly_to"]}.{dictionary[i]["fly_from"]}.{dictionary[i]["return_date"].split("T")[0]}''')
        return messages

    def organize_email(self, dictionary : dict):
        messages = []
        for i in range(len(dictionary)):
            messages.append(f'''Low price alert! Only BRL: {dictionary[i]['price']}\n
To fly from {dictionary[i]['city_from']}-{dictionary[i]['fly_from']} to {dictionary[i]['city_to']}-{dictionary[i]['fly_to']}\n
Departure date: {dictionary[i]["local_departure"].split("T")[0]}\n
Return date: {dictionary[i]["return_date"].split("T")[0]}\n
Stop over: {dictionary[i]["stop_over"]}\n
Here is a link to the for the flight: 
https://www.google.com.br/flights?hl=en#flt={dictionary[i]["fly_from"]}.{dictionary[i]["fly_to"]}.{dictionary[i]["local_departure"].split("T")[0]}*{dictionary[i]["fly_to"]}.{dictionary[i]["fly_from"]}.{dictionary[i]["return_date"].split("T")[0]}''')
        return messages
