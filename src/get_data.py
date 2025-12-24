import requests

url = "https://api.open-meteo.com/v1/forecast"

# defaults are for Salt Lake City
def get_data(variables="sunrise,sunset", latitude=40.746216, longitude=-111.905396):
    params = {
        "latitude" : latitude,
        "longitude": longitude,
        "daily"    : variables,
        "timezone" : "auto"
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    return data
