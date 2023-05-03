import os

# TODO - study a way to implement api_key through header
def set_api_key():
    # For development pourposes. Taken from https://developer.riotgames.com/
    api_key = os.getenv("RIOT_API_KEY", None) # Expires every 24 hours // I can turn this into a dependencies field
    return api_key # API key param to be used in every request
