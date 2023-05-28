import requests
import json

# Get APU from OpenWeather
API_KEY = "YOUR_API_KEY_HERE"

# Working with API to how to use it.
def get_weather_data(city, country_code):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=metric&appid={API_KEY}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None
      
 # Get input From Country or City with City name and country code
    city = input("Enter city name: ")
country_code = input("Enter country code: ")

# Print weather from city
data = get_weather_data(city, country_code)
if data:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"The temperature is {temperature} degrees Celsius and the weather is {weather}.")
else:
    print("Unable to retrieve weather information.")
