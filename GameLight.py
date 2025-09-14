from http.client import responses
import json
import requests

API_KEY = '4440531d-e039-4dcf-9b60-406486bae545'
url = 'https://openapi.api.govee.com/router/api/v1/user/devices'

headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    devices = response.json()
    print("Devices:", devices)

    print(json.dumps(devices, indent=4))
else:
    print(f"Failed to fetch devices: {response.status_code} - {response.text}")