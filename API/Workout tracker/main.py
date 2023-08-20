import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
# remove 1
API_ID = "e5fce3cb"
API_KEY = "7d05aaf5d049bdcc203910ea6ee08ba61"
today = datetime.now()

sheety_username = "sleepyroger"
sheety_password = "asdjdfoisjdfojsdifj1"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_parameter = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=nutritionix_endpoint, json=exercise_parameter, headers=headers)
result = response.json()
###################################################
basic = HTTPBasicAuth(sheety_username, sheety_password)

sheety_endpoint = "https://api.sheety.co/d34f7579daf46c0d2cca3ba848f55918/workoutTracking/workouts"
for exercise in result["exercises"]:
    sheety_parameter = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response1 = requests.post(url=sheety_endpoint, json=sheety_parameter, auth=basic)
    print(response1.text)
