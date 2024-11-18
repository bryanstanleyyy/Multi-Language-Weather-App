import sys
import requests
import os

def fetch_weather(city):
    api_key = "82cbe9c520bc7e16170e0b0bcf5e8d23"
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

         # Determine the output file path (in the Java folder's data directory)
        project_root = os.path.dirname(os.path.dirname(__file__))  # weather-app/
        output_file = os.path.join(project_root, "java/weather_data.txt")

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

