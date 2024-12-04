# Weather Forecast Application

#### Video Demo: [https://youtu.be/AggYgaLEQdM?si=u6J87QS1isaifOuA]

#### Description:

The **Weather Forecast Application** is a modern web application that provides users with real-time weather information based on any city they enter. This project leverages the power of the OpenWeatherMap API to fetch up-to-date weather data, displaying essential weather metrics such as temperature, humidity, wind speed, and weather conditions. It features an interactive user interface built with **Flask**, **HTML**, and **CSS**, and includes dynamic error handling to ensure users have a smooth experience, even in the case of invalid input or network issues.

With a visually appealing and clean design, this app displays a background image of **Azadi Tower** in Tehran, creating a local connection for users in Iran or those interested in the iconic landmark.

---

## Features

- **Real-Time Weather Data**: Fetches accurate weather data from the OpenWeatherMap API.
- **Interactive Search**: Users can input any city name to view weather details, including temperature, humidity, wind speed, and weather description.
- **Error Handling**: Displays appropriate error messages for invalid city names, network failures, and HTTP issues (e.g., city not found).
- **Dynamic Background Image**: The background of the app is an image of **Azadi Tower**, giving the app a unique and personalized touch.
- **Modern User Interface**: Responsive and clean design with easy-to-use form fields and button interactions.
- **Unit Testing**: Includes unit tests for the app's core functionality using **Pytest**.

---

## Installation

To run the Weather Forecast Application locally, follow these steps:

### Prerequisites

- **Python 3.7+**
- **pip** package manager
- **OpenWeatherMap API key** (sign up [here](https://openweathermap.org/)).

### Steps to Install

1. **Clone the Repository**:

   First, clone the project repository to your local machine:
   ```bash
   git clone https://github.com/your-repository/weather-app.git
   cd weather-app

2. Install Dependencies:
Install the required dependencies listed in the requirements.txt file using pip:
pip install -r requirements.txt
3. Set up API Key:
Create a .env file in the root directory of the project.
Add your OpenWeatherMap API key:
API_KEY=your_openweathermap_api_key
4. Run the Application:
To start the application, simply run the project.py script:
python project.py
5. Access the App:
Open your browser and go to the following URL
http://127.0.0.1:5000
6. Folder Structure
CS50-final_project/
    static/
        azadi_tower.jpg
        style.css
    template/
        index.html
    project.py
    test_project.py
    README.md
    requirements.txt
# Technologies Used
Flask (Python): A lightweight web framework used for building the server-side application.
HTML5 & CSS3: For building the structure and styling the user interface.
OpenWeatherMap API: Used to fetch weather data based on user input.
python-dotenv: A Python library to manage environment variables (like the API key).
requests: For making HTTP requests to the OpenWeatherMap API.
pytest: For unit testing the core functionality of the application.
