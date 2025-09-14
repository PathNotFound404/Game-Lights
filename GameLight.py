from http.client import responses
import json
import requests
import uuid

API_KEY = '4440531d-e039-4dcf-9b60-406486bae545'
geturl = 'https://openapi.api.govee.com/router/api/v1/user/devices'
posturl = 'https://openapi.api.govee.com/router/api/v1/device/control'
id = str(uuid.uuid4())

color = ((158 & 0xFF) << 16) | ((0 & 0xFF) << 8) | ((255 & 0xFF) << 0)

headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': API_KEY
}

payload = {
    "requestId": id,
    "payload": {
        "sku": "H6008",
        "device": "72:83:D4:AD:FC:B5:BB:EE",
        "capability": {
            "type": "devices.capabilities.color_setting",
            "instance": "colorRgb",
            "value": color
        }
    }
}

##Get call
##response = requests.get(geturl, headers=headers)

response = requests.post(posturl,headers=headers, json=payload)


if response.status_code == 200:
    devices = response.json()
    print("Devices:", devices)

    print(json.dumps(devices, indent=4))
else:
    print(f"Failed to fetch devices: {response.status_code} - {response.text}")

print(color)