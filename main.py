import requests

def make_gapi_request():
    api_key = "goldapi-hp2rsmk0bg0ar-io"
    symbol = "XAU"
    curr = "USD"
    date = "20250106"

    url = f"https://www.goldapi.io/api/{symbol}/{curr}/{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        print(result)
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
