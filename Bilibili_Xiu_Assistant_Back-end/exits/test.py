import requests

import requests
from bs4 import BeautifulSoup
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
proxies = {'http': 'proxy =47.113.196.102:22',

 }
url="http://www.overlove.xin/html/"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
req=requests.get(url,headers=header,proxies=proxies,timeout=5)
html=req.text
soup=BeautifulSoup(html,'lxml')
print(soup.text)

response = requests.get("http://httpbin.org/ip")
print(response)
