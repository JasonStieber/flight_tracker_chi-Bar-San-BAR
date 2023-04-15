import requests
import json
from config import DISCORD_WEBHOOK_URL

def send_discord_message(message):
    data = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})