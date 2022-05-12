import os
from twilio.rest import Client


class NotificationManager:
    '''Sends the message using twilio api'''

    def send_message(self, messages):
        twilio_sid = os.environ.get("TWILIO_SID")
        twilio_token = os.environ.get("TWILIO_TOKEN")

        client = Client(twilio_sid, twilio_token)
        for message in messages:
            client.messages.create(body=message,
                                   from_=os.environ.get("TWILIO_FROM"),
                                   to=os.environ.get("TWILIO_TO"))
