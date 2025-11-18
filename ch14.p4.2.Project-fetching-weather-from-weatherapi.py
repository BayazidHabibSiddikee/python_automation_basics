#! python3
import requests, sys ,pprint

if len(sys.argv) < 2:
    print("Usage: quickweather.py location")
    sys.exit()

location = ''.join(sys.argv[1:])
api_key = "4ecc4b12120d47d2a5b64407252608"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"
response = requests.get(url)
#print(response) ##
response.raise_for_status()

weather_data = response.json()

#pprint.pprint(weather_data)
# Extract info
loc = weather_data["location"]["name"]
region = weather_data["location"]["region"]
country = weather_data["location"]["country"]

condition = weather_data["current"]["condition"]["text"]
temp_c = weather_data["current"]["temp_c"]
feels_c = weather_data["current"]["feelslike_c"]

print(f"Current weather in {loc}, {region}, {country}:")
print(f"{condition}, {temp_c}°C (feels like {feels_c}°C)")
print("___________________Best of luck___________________")
