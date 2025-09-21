import requests
import os
from dotenv import load_dotenv

load_dotenv()

POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')

url = f'https://api.polygon.io/v3/reference/dividends?apiKey={POLYGON_API_KEY}'


response = requests.get(url)
print(response.json())

next_url = response.json()['next_url']

print(next_url)
data = response.json()['results']    

for ticker in data:
    print(ticker['currency'], ticker["ticker"])


