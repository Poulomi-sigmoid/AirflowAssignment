import requests
import csv


def create_new_csv():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "f9d426e936msh8f2a748d78bd155p1df405jsn4cee7b236832"
    }

    cities = ["Kolkata", "Chennai", "Bangalore", "Bhopal", "Gujarat", "Jhansi", "Shimla", "Assam", "Jaipur", "Vadodara"]
    data = []

    for city in cities:
        query = {"q": f"{city},india", "lat": "0", "lon": "0", "id": "2172797", "lang": "null",
                 "units": "imperial", "mode": "JSON"}
        response = requests.request("GET", url, headers=headers, params=query)
        result = response.json()
        weather_data = [result["name"], result["weather"][0]["description"], result["main"]["temp"],
                        result["main"]["feels_like"],
                        result["main"]["temp_min"], result["main"]["temp_max"], result["main"]["humidity"],
                        result["clouds"]["all"]]

        data.append(weather_data)

    header = ['State', 'Description', 'Temperature', 'Feels_Like_Temperature', 'Min_Temp', 'Max_Temp',
              'Humidity', 'Clouds']
    try:
        with open('country_weather.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print("Successfully completed")
    except:
        print("Could not create csv file. Unknown error occurred")
