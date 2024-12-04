import pytest
from unittest.mock import patch
from project import get_weather_data, parse_weather_data, WeatherException

@patch("project.requests.get")
def test_get_weather_data_valid(mock_get):
    """Test fetching weather data for a valid city"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "main": {"temp": 25, "humidity": 60},
        "weather": [{"description": "clear sky", "icon": "01d"}],
        "wind": {"speed": 10}
    }
    data = get_weather_data("Tehran")
    assert data["main"]["temp"] == 25
    assert data["main"]["humidity"] == 60
    assert data["wind"]["speed"] == 10

def test_get_weather_data_invalid_city():
    """Test handling invalid city name error"""
    with pytest.raises(WeatherException) as excinfo:
        get_weather_data("1234")
    assert "Invalid city name" in str(excinfo.value)

@patch("project.requests.get")
def test_get_weather_data_not_found(mock_get):
    """Test handling city not found error"""
    mock_get.return_value.status_code = 404
    mock_get.return_value.raise_for_status.side_effect = Exception("404 Client Error: Not Found for url")
    with pytest.raises(WeatherException) as excinfo:
        get_weather_data("UnknownCity")
    assert "City not found" in str(excinfo.value)

@patch("project.requests.get")
def test_get_weather_data_http_error(mock_get):
    """Test handling HTTP error"""
    mock_get.return_value.status_code = 500
    mock_get.return_value.raise_for_status.side_effect = Exception("500 Server Error: Internal Server Error for url")
    with pytest.raises(WeatherException) as excinfo:
        get_weather_data("Tehran")
    assert "HTTP error" in str(excinfo.value)

@patch("project.requests.get")
def test_get_weather_data_network_error(mock_get):
    """Test handling network error"""
    mock_get.side_effect = Exception("Network error")
    with pytest.raises(WeatherException) as excinfo:
        get_weather_data("Tehran")
    assert "Network error" in str(excinfo.value)

def test_parse_weather_data():
    """Test parsing weather data"""
    raw_data = {
        "main": {"temp": 25, "humidity": 60},
        "weather": [{"description": "clear sky", "icon": "01d"}],
        "wind": {"speed": 10}
    }
    parsed_data = parse_weather_data(raw_data)
    assert parsed_data["temperature"] == 25
    assert parsed_data["humidity"] == 60
    assert parsed_data["wind_speed"] == 10
    assert parsed_data["description"] == "clear sky"
    assert parsed_data["icon"] == "https://openweathermap.org/img/wn/01d@2x
