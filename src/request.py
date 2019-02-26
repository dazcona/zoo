import requests

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r = requests.post(url, json={
    "hair": 0,
    "feathers": 0,
    "eggs": 1,
    "milk": 0,
    "airborne": 0,
    "aquatic": 1,
    "predator": 1,
    "toothed": 1,
    "backbone": 1,
    "breathes": 1,
    "venomous": 1,
    "fins": 0,
    "legs": 4,
    "tail": 0,
    "domestic": 0,
    "catsize": 0,
})

print(r.json())