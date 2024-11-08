import requests
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = {}
    error = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            api_key = os.getenv("WEATHER_API_KEY")
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url).json()
            
            # Check if response contains 'main' to confirm city is found
            if response.get("main"):
                weather = {
                    "city": response["name"],
                    "temp": response["main"]["temp"],
                    "feels_like": response["main"]["feels_like"],
                    "humidity": response["main"]["humidity"],
                    "description": response["weather"][0]["description"].capitalize(),
                    "icon_url": f"http://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png",
                    "wind_speed": response["wind"]["speed"],
                    "pressure": response["main"]["pressure"]
                }
            else:
                # Handle case where city is not found
                error = "City not found. Please enter a valid city name."
    
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
