import requests

SHEETY_API = "https://api.sheety.co/c0a871fe29358068d2074551e0b27f5a/flightdeals/users"

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
while True:
    email = input("What is your email?: ")
    if email == input("Type your email again: "):
        break
    else:
        print("The emails did not match")

shetty_parameters = {"user" : {"firstName" : first_name,
                               "lastName" : last_name,
                               "email" : email
                               }
                     }

request = requests.post(url=SHEETY_API, json=shetty_parameters)
print("Registration complete!")
