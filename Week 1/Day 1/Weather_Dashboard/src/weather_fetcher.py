import os
import sys

# Add the utils folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), "../utils"))

from utils import save_to_local, upload_to_s3, fetch_weather

def main():
    city = "Addis Ababa"  # Replace with desired city
    bucket_name = "weather-data"

    print(f"Fetching weather data for {city}...")
    weather_data = fetch_weather(city)

    if weather_data:
        file_name = f"{city.replace(' ', '_')}_weather.json"
        save_to_local(weather_data, file_name)
        upload_to_s3(file_name, bucket_name)

if __name__ == "__main__":
    main()
