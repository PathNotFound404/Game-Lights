from http.client import responses
import json
from time import sleep
import requests
import uuid
import config
from PIL import ImageGrab
import numpy as np

#url to post request
posturl = 'https://openapi.api.govee.com/router/api/v1/device/control'






#Function to change the color of each light in the Device List
def change_color(color):


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


def make_color_int(r, g, b) -> int:
        rgb = ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | ((b & 0xFF) << 0)
        return rgb

def get_avg_color() -> int:
    ##Get Screenshot then make array
    img = ImageGrab.grab()
    ##img_np = np.array(img)

    img_arr = np.frombuffer(img.tobytes(), dtype=np.uint8)
    img_arr = img_arr.reshape((img.size[1], img.size[0], 3))


    """"Speed this up using mean and int casting"""
    ##Get avg color of image
    step = 25
    num_pixels = 1080//step * 1920//step
    r = g = b = 0

    for y in range(0, 1080, step):
        for x in range(0, 1920, step):
            px = img_arr[y][x]
            r += px[0]
            g += px[1]
            b += px[2]
    r = r//num_pixels
    g = g//num_pixels
    b = b//num_pixels

    color = make_color_int(r,g,b)

    img.close()
    return color



while True:
    change_color(int(get_avg_color()))
    print(get_avg_color())



