import requests
from urllib.parse import urlparse

url = input('Enter domain url: ')
urlParse = urlparse(url)
sub, host, tld = urlParse.netloc.split('.')
domain = f'{host}.{tld}'
# print(urlParse.path)
protocol = urlParse.scheme

file = open('subdomain.txt','r')
content = file.read()
subdomainsList = content.splitlines()

discoveredDomains = []
for subdomain in subdomainsList:
    searchurl = f'{protocol}://{subdomain}.{domain}'
    try:
        r = requests.get(searchurl)
    except requests.ConnectionError:
        pass
    else:
        print(f'[+] Discovered subdomains: {searchurl} Status code: {r.status_code}')
        discoveredDomains.append(searchurl)
