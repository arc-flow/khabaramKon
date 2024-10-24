import requests

#sending the user prompt
def post_data(api_url, data, headers):
    try:
        response = requests.post(api_url, json=data, headers=headers)  # Posting data as JSON
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")