import requests


def get_data() -> dict:
    headers = {'Content-Type': 'application/json'}
    response = requests.get("https://example.com/data", headers=headers)
    return response.json()

def post_data(data: dict) -> dict:
    headers = {'Content-Type': 'application/json'}
    response = requests.post("https://example.com/data", headers=headers, json=data)
    print(response.text)
    return response.json()
