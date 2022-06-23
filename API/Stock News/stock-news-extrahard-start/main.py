import os
import requests
import datetime as dt
from twilio.rest import Client

# -------------------- Variables --------------------#
# Stock information
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Api information
parameters_alpha_vantage = {"apikey" : "J1LTK9YY3Q5O8GEV",  # os.environ.get("alpha_key")
                            "function" : "TIME_SERIES_Daily",
                            "symbol" : "IBM",}
parameters_news_api = {"apiKey" : "248b6c91329f42cc8a07b32321017c3d",
                       "qInTitle" : COMPANY_NAME,}
twilio_token = "737dda2df373d4f57e8d48b23bc325b2"
twilio_sid = "ACc947842d7f71f13ecf987646f73e196e"

# Date information
date = dt.datetime.now()
week_day = date.isoweekday()
if week_day == 7:
    yest = 2
    d_b_y = 3
elif week_day == 1:
    yest = 3
    d_b_y = 4
elif week_day == 2:
    yest = 1
    d_b_y = 4
else:
    yest = 1
    d_b_y = 2
yesterday = "{:02d}".format(date.day - yest)
day_before_yesterday = "{:02d}".format(date.day - d_b_y)
month = "{:02d}".format(date.month)

# -------------------- APIs --------------------#
# Gets the stock market prices
request_stocks = requests.get(f"https://www.alphavantage.co/query?", params=parameters_alpha_vantage)
request_stocks.raise_for_status()
data_stock = request_stocks.json()
yestday_market = float(data_stock["Time Series (Daily)"][f"{date.year}-{month}-{yesterday}"]["4. close"])
day_before_market = float(data_stock["Time Series (Daily)"][f"{date.year}-{month}-{day_before_yesterday}"]["4. close"])

# Formats the percentage for the message
diff = yestday_market - day_before_market
percentage = round(diff / float(yestday_market) * 100)
if diff > 0:
    msg = f"🔺 {percentage}"
else:
    msg = f"🔻 {percentage}"

# Gets the stock news
request_news = requests.get("https://newsapi.org/v2/everything", params=parameters_news_api)
request_news.raise_for_status()
data_news = request_news.json()["articles"]
articles = data_news[:3]
formatted_article = [f"{STOCK} : {msg}%\nHeadline:{article['title']}\nBrief: {article['description']}" for article in articles]

# Sends a message with the information
client = Client(twilio_sid, twilio_token)
for article in formatted_article:
    client.messages.create(body=article,
                           from_="+19896468385",
                           to="+55 99 98510 3232")
