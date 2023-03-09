import requests

API_KEY = "2126afd36365dd31cdac54c1fbb9d26c"
def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_of_forecasts = 8 * forecast_days
    filtered_data = filtered_data[:nr_of_forecasts]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=2))