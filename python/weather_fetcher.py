import sys
import requests

def fetch_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()

        # Extract relevant weather info
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

        # Write to a file for Java to read
        with open("weather_data.txt", "w") as file:
            file.write(f"City: {weather_info['city']}\n")
            file.write(f"Temperature: {weather_info['temperature']} °C\n")
            file.write(f"Description: {weather_info['description']}\n")

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weather_fetcher.py [city_name]")
        sys.exit(1)

    fetch_weather(sys.argv[1])

