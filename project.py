# Woman_Life_Freedom
from flask import Flask, request, render_template, jsonify
import requests
import os
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API Key is missing! Please make sure to add it to your .env file.")

# Flask settings
app = Flask(__name__, template_folder='template', static_folder='static')

class WeatherException(Exception):
    """Exception for handling weather-related errors"""
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Code: {self.code})" if self.code else self.message

def get_weather_data(city):
    """Get weather data from the API"""
    if not re.match(r"^[a-zA-Z\s]+$", city):
        raise WeatherException("Invalid city name. Please use letters only.", code=400)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            raise WeatherException("City not found!", code=404)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise WeatherException(f"HTTP error: {str(e)}", code=response.status_code)
    except requests.exceptions.RequestException as e:
        raise WeatherException(f"Network error: {str(e)}")

def parse_weather_data(data):
    """Parse the data and extract key weather information"""
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
        "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    }

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page of the app"""
    weather_info = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        try:
            raw_data = get_weather_data(city)
            weather_info = parse_weather_data(raw_data)
        except WeatherException as e:
            error_message = str(e)

    return render_template("index.html", weather=weather_info, error=error_message)

@app.route("/api/weather", methods=["GET"])
def api_weather():
    """API for getting weather information"""
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400
    try:
        raw_data = get_weather_data(city)
        weather_data = parse_weather_data(raw_data)
        return jsonify(weather_data)
    except WeatherException as e:
        return jsonify({"error": str(e)}), e.code if e.code else 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
