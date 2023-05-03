import os

# TODO - study a way to implement api_key through header
async def set_api_key():
    # For development pourposes. Taken from https://developer.riotgames.com/
    # "RGAPI-a19df1f2-7b5a-4bc1-a922-c932e9a98c7a"
    api_key = os.getenv("RIOT_API_KEY", None) # Expires every 24 hours // I can turn this into a dependencies field
    # return f"api_key={api_key}" # API key param to be used in every request
    return api_key
