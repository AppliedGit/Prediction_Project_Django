import json
import requests
import pickle
import numpy as np
import sklearn
import jwt 
import datetime
import uuid
import hashlib
import pandas as pd


car_config = {
    'Year': 2014,
    'Present_Price': 10.5,
    'Kms_Driven': 43000,
    'Owner': 0,
    'Fuel_Type_Petrol': 'Diesel',
    'Seller_Type_Individual': 'Dealer',
    'Transmission_Mannual': 'Manual'
}

#print(car_config)
#url = "https://ml.appliediiot.com/gettoken"
#res = requests.get(url)
#res_str = res.text
#res_json_arr = json.loads(res_str)
#token = res_json_arr["token"]
#time.sleep(2)
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMDIwZDc3MTY5ZWUzNDYwNTllOGEyMjMzYmRmNWUwYTQiLCJleHAiOjE2NDE0NDMzNDF9.0zNkygOraiOMPSid94E7vd5aF62xUZ9saAvauRSK00M'
url = "https://ml.appliediiot.com/carpredict?token="+token
#url = "http://127.0.0.1:5000/carpredict?token="+token
r = requests.post(url, json = car_config)
prediction_json_arr = json.loads(r.text)
try:
    print(prediction_json_arr["car_prediction"])
except Exception as e:
    print(prediction_json_arr["message"])
