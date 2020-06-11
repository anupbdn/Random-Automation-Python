import requests

try:
    response = requests.get('https://admin-tuclothing.sainsburys.co.uk', timeout=8)
    return_response = response.status_code

except:
    print('No response')