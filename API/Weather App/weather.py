import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

token = os.environ.get('TOKEN')
sid = os.environ.get("SID")

parameters = {
    "lat" : -13.454338,
    "lon" : -16.533669,
    "api_key" : "76c066754b3109f283771146a63a3fee",
    "exclude" : "current, minutely, daily",
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={parameters['lat']}&lon={parameters['lon']}&exclude={parameters['exclude']}&appid={parameters['api_key']}")
response.raise_for_status()
data = response.json()
for i in range(0, 12):
    if (data["hourly"][i]["weather"][0]["id"]) < 700:
        print(f"{i} Bring a umbrella")
        print(data["hourly"][i]["weather"][0]["id"])
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {"https" : os.environ["https_proxy"]}
        client = Client(sid, token) # http_client=proxy_client
        message = client.messages.create(body="Teste de Api",
        from_ = "+19896468385",
        to = "+55 99 98510 3232")
        print("Done")
        break
