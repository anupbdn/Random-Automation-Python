import csv
import requests

with open('websites.csv',newline='') as websites:
    websites_dict = csv.DictReader(websites)
    
    for url in websites_dict:
        website = url['URL']
        url_to_check = 'https://'+website
        try:
            response = requests.get(url_to_check, timeout=10)
            website_status_code = response.status_code
            print(f'{website},{website_status_code}')
            
        except:
            print(f'{website},URL not responding')
        #print(f'{website},{website_status_code}')
            

# url = ['outlook.office365.com','google.com']

# for i in url:
#     url = 'https://'+i
#     response = requests.get(url)
#     status = response.status_code
#     print(f'{url} {status}')