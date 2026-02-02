import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()


def get_weather_data(location: str, r):

    BASE_URL = os.getenv("WEATHER_API_BASE_URL")
    API_KEY = os.getenv("WEATHER_API_KEY")

    if not BASE_URL or not API_KEY:
        raise RuntimeError("Weather API env vars not set")

    cached_response = r.get(f"{location}")
    print(f"--cached response: {cached_response}")
    if cached_response is None:
        endpoint = f"{BASE_URL}/{location}?key={API_KEY}"
        print(f"--endpoint {endpoint}")
        response = requests.get(endpoint, timeout=5)
        r.setex(f"{location}", 600, json.dumps(response.json()))

    else:
        return json.loads(cached_response)

    # Explicitly handle HTTP errors
    response.raise_for_status()

    return response.json()
