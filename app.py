
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Ranchi, Jharkhand
LATITUDE = 23.3441
LONGITUDE = 85.3096


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/weather")
def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
            "current": [
  		  "temperature_2m",
    		"relative_humidity_2m",
   		 "apparent_temperature",
    		"is_day",
    		"precipitation",
    		"wind_speed_10m",
    		"weather_code",
    		"pressure_msl",
    		"uv_index"
        ],
        "hourly": [
            "temperature_2m",
            "precipitation_probability",
            "weather_code"
        ],
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max"
        ],
        "timezone": "Asia/Kolkata",
        "forecast_days": 5
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as error:
        return jsonify({"error": "Unable to fetch weather data",
                        "details": str(error)}), 502


if __name__ == "__main__":
    app.run(debug=True)
