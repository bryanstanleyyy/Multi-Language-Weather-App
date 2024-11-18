# Multi-Language Weather App

The **Multi-Language Weather App** is a simple project that combines Python and Java to retrieve and display real-time weather data. Python fetches weather details from the OpenWeatherMap API, while Java provides a graphical interface to present the information.

## Features

- Fetches real-time weather data (temperature, description) for any city.
- Displays the weather data in a Java-based GUI.
- Demonstrates interoperation between Python and Java.

## Prerequisites

### Software
- Python 3.x
- Java Development Kit (JDK) 8 or later

### Python Libraries
Install the required Python libraries using:
```bash
pip install -r python/requirements.txt
```

Add the following to `requirements.txt`:
```
requests
```

## Project Structure

```
weather-app/
├── python/
│   ├── weather_fetcher.py        # Fetches weather data using Python
│   ├── requirements.txt          # Required Python libraries
├── java/
│   ├── WeatherApp.java           # Displays weather data in a Java GUI
│   ├── weather_data.txt          # Temporary file to store weather data
├── README.md                     # Project documentation
```

## Usage

### Clone this repository:
```bash
git clone https://github.com/bryanstanleyyy/Timezone-Converter.git
cd Timezone-Converter/src
```

### Step 1: Fetch Weather Data with Python
1. Navigate to the `python` directory:
   ```bash
   cd python
   ```
2. Run the Python script to fetch weather data for a city:
   ```bash
   python weather_fetcher.py "CityName"
   ```
   Replace `"CityName"` with the name of the city you want to fetch the weather for (e.g., `London`).

3. Check that the file `weather_data.txt` is generated in the `java` directory.

### Step 2: Run the Java Application
1. Navigate to the `java` directory:
   ```bash
   cd ../java
   ```
2. Compile the Java program:
   ```bash
   javac WeatherApp.java
   ```
3. Run the Java program:
   ```bash
   java WeatherApp
   ```

4. The GUI window will open, displaying the weather data.

## Example Workflow

1. Run the Python script:
   ```bash
   python weather_fetcher.py "New York"
   ```

2. Output in `weather_data.txt`:
   ```
   City: New York
   Temperature: 22.5 °C
   Description: clear sky
   ```

3. Launch the Java GUI, which displays:
   ```
   City: New York
   Temperature: 22.5 °C
   Description: clear sky
   ```

## Improvements

- Use real-time communication (e.g., sockets) between Python and Java instead of file-based interaction.
- Add a search feature in the GUI for dynamic weather retrieval.
- Extend weather details to include humidity, wind speed, and a 5-day forecast.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
