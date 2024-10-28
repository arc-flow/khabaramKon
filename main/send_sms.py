from kavenegar import *

def sendMessange(msg, receptor):
    api = KavenegarAPI("6255497A36346F58334655592F746F7463455377774C5577332B48413153325730774F48396A436B486D633D")
    try:
        params = {'sender': '200090908000', 'receptor': receptor, 'message': msg}
        api.sms_send(params)
    except Exception as e:
        print(e)

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
