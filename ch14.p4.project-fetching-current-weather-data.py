#! python3
import requests, json, sys, webbrowser

#get location from cli and browse to OpenWeatherMap.org or www.weatherapi.com
if len(sys.argv)<2: #basically unimportant but I can't make the user think -_-
	print('Usage: quickweather.py location')
	sys.exit()
location = ''.join(sys.argv[1:])
api_key = '4ecc4b12120d47d2a5b64407252608'

#Now download the data from OpenWeatherMap.org's API
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes'
#url =f'http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3'
response = requests.get(url)
response.raise_for_status()

#Load json data in python module
weather_data = {
  "location": {
    "name": "London",
    "region": "City of London, Greater London",
    "country": "United Kingdom",
    "lat": 51.5171,
    "lon": -0.1062,
    "tz_id": "Europe/London",
    "localtime_epoch": 1756192115,
    "localtime": "2025-08-26 08:08"
  },
  "current": {
    "last_updated_epoch": 1756191600,
    "last_updated": "2025-08-26 08:00",
    "temp_c": 17.4,
    "temp_f": 63.3,
    "is_day": 1,
    "condition": {
      "text": "Sunny",
      "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
      "code": 1000
    },
    "wind_mph": 8.5,
    "wind_kph": 13.7,
    "wind_degree": 240,
    "wind_dir": "WSW",
    "pressure_mb": 1007,
    "pressure_in": 29.74,
    "precip_mm": 0,
    "precip_in": 0,
    "humidity": 68,
    "cloud": 0,
    "feelslike_c": 17.4,
    "feelslike_f": 63.3,
    "windchill_c": 20.2,
    "windchill_f": 68.3,
    "heatindex_c": 20.2,
    "heatindex_f": 68.3,
    "dewpoint_c": 11.9,
    "dewpoint_f": 53.4,
    "vis_km": 10,
    "vis_miles": 6,
    "uv": 0.6,
    "gust_mph": 10,
    "gust_kph": 16.2,
    "air_quality": {
      "co": 358.9,
      "no2": 66.415,
      "o3": 31,
      "so2": 4.81,
      "pm2_5": 18.13,
      "pm10": 28.49,
      "us-epa-index": 2,
      "gb-defra-index": 2
    },
    "short_rad": 122.3,
    "diff_rad": 60.16,
    "dni": 464.19,
    "gti": 135.22
  }
}
#Now print it
w = weather_data['list']
print(f'Current weather in {location}:')
print(w[0]['weather'][0]['main'],'-',w[0],['weather'][0]['description'])
print()
print(f'Tomorrow weather in {location}:')
print(w[1]['weather'][1]['main'],'-',w[1],['weather'][1]['description'])
print()
print(f'Current weather in {location}:')
print(w[2]['weather'][2]['main'],'-',w[2],['weather'][2]['description'])
print('___________________Best of luck___________________')
