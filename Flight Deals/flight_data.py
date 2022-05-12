# coding=utf8

class FlightData:
    '''Formats the dictionary information into a message to be sent'''

    def organize(self, dictionary : dict):
        messages = []
        for i in range(len(dictionary)):
            messages.append(f'''Low price alert! Only R${dictionary[i]['price']}\n
To fly from {dictionary[i]['city_from']}-{dictionary[i]['fly_from']} to {dictionary[i]['city_to']}-{dictionary[i]['fly_to']}\n
Departure date: {dictionary[i]["local_departure"].split('T')[0]}''')
        return messages
