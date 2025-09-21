import requests
import json
import config

url = 'https://openapi.api.govee.com/router/api/v1/user/devices'

headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': config.api_key
}
response = requests.get(url, headers=headers)


#Print out the Device information in readable formate or return error code
if response.status_code == 200:
    devices = response.json()
    out = "devices.txt"
    with open(out,'w') as json_file:
        json.dump(devices, json_file, indent=4)

else:
    print(f"Failed to fetch devices: {response.status_code} - {response.text}")