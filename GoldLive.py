import requests
import json
import os


BLOOM_KEY = os.environ.get('METAL_KEY')
BLOOM_HOST = os.environ.get('METAL_HOST')

url = "https://live-metal-prices.p.rapidapi.com/v1/latest/XAU,XAG,PA,PL,GBP,EUR/INR/gram"

headers = {
	"X-RapidAPI-Key": METAL_KEY,
	"X-RapidAPI-Host": METAL_HOST
}

response = requests.get(url, headers=headers)

print(response.json())