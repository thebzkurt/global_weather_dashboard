import requests
import matplotlib.pyplot as plt

API_KEY = 'your api key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    params = {
        "q": city,
        "APPID": API_KEY,
        "units": "metric",
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data {response.status_code}")
        return None

def display_weather_data(data):
    print("---------------------")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind: {data['wind']['speed']}m/s")
    print(f"weather: {data['weather'][0]['description'].title()}")

def plot_weather_trend(days, temperature):
    plt.plot(days, temperature, marker='o', color='r')
    plt.title('Temperature trend')
    plt.xlabel('Days')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.show()

def compare_weather(cities):
    temps = []
    for city in cities:
        data = fetch_weather_data(city)
        if data:
            temps.append((city, data['main']['temp']))

        city_names = [t[0] for t in temps]
        city_temps = [t[1] for t in temps]

        plt.bar(city_names, city_temps, color='r')
        plt.title("Temperature Comparison")
        plt.xlabel('City')
        plt.ylabel('Temperature')
        plt.show()

def main():
    print("Welcome to Global Weather Dashboard")
    while True:
        print("\nMenu:")
        print("1. View weather for a city")
        print("2. Compare weather for multiple cities")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter city: ")
            weather_data = fetch_weather_data(city)
            if weather_data:
                display_weather_data(weather_data)
        elif choice == '2':
            cities = input("Enter city names separated by comma: ").split(',')
            compare_weather([city.strip() for city in cities])
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
