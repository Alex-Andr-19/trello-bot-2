import requests
import json

webhook_url = 'https://trello-webhook-telegram.herokuapp.com/webhook'

data = {'asfdads':'as'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'aplication/json'})