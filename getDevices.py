import requests
import json


url = 'https://openapi.api.govee.com/router/api/v1/user/devices'
api_key = '4440531d-e039-4dcf-9b60-406486bae545'

headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': api_key
}
response = requests.get(url, headers=headers)


#Print out the Device information in readable formate or return error code
if response.status_code == 200:
    devices = response.json()
    print(json.dumps(devices, indent=4))
else:
    print(f"Failed to fetch devices: {response.status_code} - {response.text}")