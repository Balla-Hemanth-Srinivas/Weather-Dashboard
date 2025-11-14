import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("YOUR_API_KEY")

def fetch_weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    try:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch weather data.")
        return None

def display_weather(data):
    """Display weather details in a clean format."""
    if not data:
        return

    print("\n=== Weather Dashboard ===")
    print(f"City         : {data['name']}")
    print(f"Temperature  : {data['main']['temp']}°C")
    print(f"Feels Like   : {data['main']['feels_like']}°C")
    print(f"Humidity     : {data['main']['humidity']}%")
    print(f"Wind Speed   : {data['wind']['speed']} m/s")
    print(f"Condition    : {data['weather'][0]['description'].title()}")
    print("==========================\n")

def main():
    print("Weather Dashboard App")
    print("----------------------")
    print("Enter city name followd by comma and Country code.")
    city = input("Eg: Hyderabad,IN :").strip()

    data = fetch_weather(city)
    display_weather(data)

if __name__ == "__main__":
    main()
