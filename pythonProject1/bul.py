import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input("url")
ml = urllib.request.urlopen(url).read()
soup = BeautifulSoup(ml , 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href' , None))