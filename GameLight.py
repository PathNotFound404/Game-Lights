from http.client import responses
import json
from time import sleep
import requests
import uuid
import config

#url to post requst
posturl = 'https://openapi.api.govee.com/router/api/v1/device/control'






#Function to change the color of each light in the Device List
def change_color(r, g, b,):
    color = ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | ((b & 0xFF) << 0)

    for d in config.devices:
        request_id = str(uuid.uuid4())

        headers = {
            'Content-Type': 'application/json',
            'Govee-API-Key': config.api_key
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






