import requests

API_KEY = "d56f71df03840b306d976ff760f120e0" 
CITY = "Kanpur"

def get_weather_data():
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        )
        if response.status_code == 200:
            data = response.json()
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"{description}, {temp}°C"
        else:
            return "Weather info not available"
    except Exception as e:
        return "Weather API error"