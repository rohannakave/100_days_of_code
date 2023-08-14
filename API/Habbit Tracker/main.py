import requests
from datetime import datetime

USERNAME = "sleepyroger"
TOKEN = "hsfhdfsjkhd"
ID = "graph1"
today = datetime.now()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_parameter = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameter)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_parameter = {
    "id": ID,
    "name": "Learning graph",
    "unit": "Hrs",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response1 = requests.post(url=graph_endpoint, json=graph_parameter, headers=headers)
# print(response1.text)

graph_post_endpoint = f"{graph_endpoint}/{ID}"
graph_post_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours have you studied today? ")
}

# response2 = requests.post(url=graph_post_endpoint, json=graph_post_parameter, headers=headers)
# print(response2.text)

pixela_update_endpoint = f"{graph_post_endpoint}/20230812"
update_parameter = {
    "quantity": "0.5"
}

# response3 = requests.put(url=pixela_update_endpoint, json=update_parameter, headers=headers)
# print(response3.text)

delete_endpoint = pixela_update_endpoint

response4 = requests.delete(url=delete_endpoint, headers=headers)
print(response4.text)
