import requests

# Replace 'your_api_key' with your actual API key from OpenWeatherMap
API_KEY = "863f690dd8dc60142c4a1423a30715ba"
BASE_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'

def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_temperature(weather_data, target_date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(target_date):
            return entry['main']['temp']
    return None

def get_wind_speed(weather_data, target_date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(target_date):
            return entry['wind']['speed']
    return None

def get_pressure(weather_data, target_date):
    for entry in weather_data['list']:
        if entry['dt_txt'].startswith(target_date):
            return entry['main']['pressure']
    return None

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather_data(city)
    if weather_data is None:
        return

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("No data available for the given date.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No data available for the given date.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data available for the given date.")

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()