from http.client import responses
import json
from time import sleep
import requests
import uuid



API_KEY = '4440531d-e039-4dcf-9b60-406486bae545'
geturl = 'https://openapi.api.govee.com/router/api/v1/user/devices'
posturl = 'https://openapi.api.govee.com/router/api/v1/device/control'

#List of device ID numbers of the lights to change
devices = ["00:68:D4:AD:FC:E6:F3:4E","FB:EA:D4:AD:FC:E6:F6:74"]



#Function to change the color of each light in the Device List
def change_color(r, g, b,):
    color = ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | ((b & 0xFF) << 0)

    for d in devices:
        request_id = str(uuid.uuid4())

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': API_KEY
        }

        payload = {
            "requestId": request_id,
            "payload": {
                "sku": "H6008",
                "device": d,
                "capability": {
                    "type": "devices.capabilities.color_setting",
                    "instance": "colorRgb",
                    "value": color
                }
            }
        }
        response = requests.post(posturl,headers=headers, json=payload)
        if response.status_code == 200:
            continue
        else:
            print(f"Failed to fetch devices: {response.status_code} - {response.text}")


change_color(255,0,0)
##sleep(.1)
change_color(0,255,0)
##sleep(.1)
change_color(0,0,255)
print("done")






