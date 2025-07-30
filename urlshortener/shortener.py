import requests, json
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv('API_KEY')

UI = input("Enter a URL: ")

data = {"long_url": UI}

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

results = requests.post(
    "https://api-ssl.bitly.com/v4/shorten",
    headers = headers,
    data = json.dumps(data)
)

link = json.loads(results.content)

print(link['link'])

