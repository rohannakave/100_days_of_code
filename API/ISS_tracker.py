import requests
from datetime import datetime

time_now = datetime.now().hour
MY_LAT = 18.579354
MY_LNG = 73.685002

def is_iss_overhead():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    r.raise_for_status()
    data = r.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True

def is_night():
    parameter = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameter)
    response.raise_for_status()
    data1 = response.json()
    sunrise = int(data1['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data1['results']['sunset'].split('T')[1].split(':')[0])
    if time_now >= sunset and time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    print("look up")
