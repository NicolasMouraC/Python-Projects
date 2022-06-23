import os
import datetime
import requests

NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY") # "ab227358e74e765276bb5666febd0a86"
NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID") # '2c3e059c'

nutritionix_headers = {"x-app-id" : NUTRITIONIX_ID,
                       "x-app-key" : NUTRITIONIX_KEY,
                       "x-remote-user-id" : "0"}
exercise_parameters = {"query" : input("?: "),
                       "gender" : "male",
                       "weight_kg" : "70",
                       "height_cm" : "175",
                       "age" : "18"}

base_url = os.environ.get("BASE_URL") # "https://trackapi.nutritionix.com/"
exercise_url = f"{base_url}v2/natural/exercise"

request = requests.post(url=exercise_url, json=exercise_parameters, headers=nutritionix_headers)
data = request.json()["exercises"][0]

date = datetime.datetime.now()

sheety_parameters = {"workout" : {"date" : f"{date.strftime('%d/%m/%Y')}",
                                  "time" : f"{date.strftime('%X')}",
                                  "exercise" : f"{data['name'].title()}",
                                  "duration" : f"{data['duration_min']}",
                                  "calories" : f"{data['nf_calories']}"
                                  }
                     }
sheety_header = {"Content-Type" : "application/json",
                 "Authorization" : "Bearer asdfghjs"}

post_sheety = "https://api.sheety.co/c0a871fe29358068d2074551e0b27f5a/workout/workouts"
request_sheety = requests.post(url=post_sheety, json=sheety_parameters, headers=sheety_header)
print(request_sheety.text)
