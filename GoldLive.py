import requests
import json
import os


METAL_KEY = os.environ.get('METAL_KEY')
METAL_HOST = os.environ.get('METAL_HOST')

url = "https://live-metal-prices.p.rapidapi.com/v1/latest/XAU,XAG/INR/gram"

headers = {
	"X-RapidAPI-Key": METAL_KEY,
	"X-RapidAPI-Host": METAL_HOST
}

response = requests.get(url, headers=headers)

response = requests.get(url, headers=headers)

loadJsonData = response.json()

InitializationX = json.dumps(loadJsonData)
DeinitilizationY = json.loads(InitializationX)

buyCcy = DeinitilizationY['baseCurrency']
buyUnit = DeinitilizationY['unit']
GoldRate = DeinitilizationY['rates']['XAU']
SilverRate = DeinitilizationY['rates']['XAG']

print('1 {1} XAU = {2} {0}'.format(buyCcy, buyUnit, round(GoldRate,2)))
print('1 {1} XAG = {2} {0}'.format(buyCcy, buyUnit, round(SilverRate,2)))
