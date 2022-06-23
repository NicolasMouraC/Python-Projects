from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# ------------------------------ USERFUL INFORMATION ------------------------------ #

# To run this file you have to set the following environment variables in the shell:
# TEQUILA_ENDPOINT -> Tequila endpoint provided by the kiwi api
# TEQUILA_KEY -> Tequila key from the kiwi api
# TWILIO_SID -> Twilio sid from the website
# TWILIO_TOKEN -> Twilio token from the website
# TWILIO_FROM -> The cellphone number to send message
# TWILIO_TO -> The cellphone number to receive the message

__author__ = "Nicolas de Moura"
__github__ = "https://github.com/NicolasMouraC"
__date__ = "11/05/2022"

# ------------------------------ Script ------------------------------ #
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

sheets_data = data_manager.get_data()
flights_on_sale = flight_search.flight_search(sheets_data)
messages = flight_data.organize_sms(flights_on_sale)

notification_manager.send_message(messages)
notification_manager.send_email(messages)
