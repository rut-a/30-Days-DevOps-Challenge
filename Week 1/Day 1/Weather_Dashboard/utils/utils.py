import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def save_to_local(data, file_name, directory="../data"):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as file:
        json.dump(data, file)
    print(f"Data saved locally at {file_path}")

def upload_to_s3(file_name, bucket_name, directory="../data"):
    import boto3

    s3 = boto3.client(
        "s3",
        endpoint_url=os.getenv("LOCALSTACK_ENDPOINT"),
        aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
        region_name="us-east-1",
    )
    file_path = os.path.join(directory, file_name)
    try:
        s3.upload_file(file_path, bucket_name, file_name)
        print(f"Uploaded {file_name} to bucket {bucket_name}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")
