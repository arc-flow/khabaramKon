import requests
from kavenegar import *


#sending the user prompt
def post_data(api_url, data, headers):
    try:
        response = requests.post(api_url, json=data, headers=headers)  # Posting data as JSON
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def send_otp(phone, otp):
    try:
        api = KavenegarAPI('6255497A36346F58334655592F746F7463455377774C5577332B48413153325730774F48396A436B486D633D')
        params = {
            'receptor': phone,
            'template': 'verify',
            'token': str(otp),
            'type': 'sms',
        }
        response = api.verify_lookup(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
