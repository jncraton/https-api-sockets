import requests
import sys

sentence = " ".join(sys.argv[1:])

response = requests.post("https://joncraton.com/sentiment", data=sentence)

print(response.text)
