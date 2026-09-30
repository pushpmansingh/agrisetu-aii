import requests


COUNTRY_CODES = {
    "Brazil": "BR",
    "Russia": "RU",
    "India": "IN",
    "China": "CN",
    "South Africa": "ZA",
}


def get_weather(location, country):

    country_code = COUNTRY_CODES.get(country)

    try:
        # Step 1: Convert location name into latitude and longitude
        geocoding_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": location,
                "countryCode": country_code,
                "count": 1,
                "language": "en",
            },
            timeout=15
        )

        geocoding_response.raise_for_status()

        location_data = geocoding_response.json()

        if not location_data.get("results"):
            return {
                "error": "Location not found. Please enter a more specific city or district."
            }

        place = location_data["results"][0]

        latitude = place["latitude"]
        longitude = place["longitude"]

        # Step 2: Get real weather and environmental data
        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": ",".join([
                    "temperature_2m",
                    "relative_humidity_2m",
                    "apparent_temperature",
                    "precipitation",
                    "weather_code",
                    "wind_speed_10m",
                    "soil_temperature_6cm",
                    "soil_moisture_3_to_9cm",
                ]),
                "daily": ",".join([
                    "weather_code",
                    "temperature_2m_max",
                    "temperature_2m_min",
                    "precipitation_sum",
                    "precipitation_probability_max",
                    "wind_speed_10m_max",
                    "et0_fao_evapotranspiration",
                ]),
                "forecast_days": 7,
                "timezone": "auto",
            },
            timeout=15
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        return {
            "location": place["name"],
            "admin_area": place.get("admin1", ""),
            "country": place.get("country", country),
            "latitude": latitude,
            "longitude": longitude,
            "current": weather_data.get("current", {}),
            "daily": weather_data.get("daily", {}),
        }

    except requests.exceptions.Timeout as error:

        print("Weather API Timeout:", error)

        return {
            "error": (
                "The weather service is taking longer than expected. "
                "Please try again in a moment."
            )
        }

    except requests.exceptions.RequestException as error:

        print("Weather API Error:", error)

        return {
            "error": (
                "We could not fetch weather information right now. "
                "Please check your connection and try again."
            )
        }