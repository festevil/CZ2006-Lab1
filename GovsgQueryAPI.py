import urllib.request
import requests
import json
from urllib.request import Request, urlopen

url = 'https://data.gov.sg/api/action/datastore_search?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee&limit=100'
#req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()
dict = requests.get(url).json()
for i in range(0,100):
    if (int(dict['result']['records'][i]['resale_price']) <= 250000):
        print(dict['result']['records'][i])
#fileobj = urllib.request.urlopen(url)
#print(webpage)
#with urllib.request.urlopen(url) as f:
#    print(f.read().decode('utf-8'))