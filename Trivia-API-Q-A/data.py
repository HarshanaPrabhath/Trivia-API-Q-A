import requests
import json

parameters = {
    "amount": 10,
    "type": "boolean",
}

response_api = requests.get("https://opentdb.com/api.php", params=parameters)
data = response_api.json()

question_data = data["results"]

