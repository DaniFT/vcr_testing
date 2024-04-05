import requests


def fetch_data() -> dict:
    headers = {'Content-Type': 'application/json'}
    response = requests.get("https://example.com/data", headers=headers)
    return response.json()
