import requests
import json
import sys

text = ' '.join(sys.argv[1:])

response = requests.post(
    "https://sentim-api.herokuapp.com/api/v1/",
    headers={"accept": "application/json", "content-type": "application/json"},
    data=json.dumps({"text": text})
)

print(response.json()["result"]["polarity"])
