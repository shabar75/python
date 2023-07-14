# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# url = input('url' '')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html , 'html.parser')
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href' , None))

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# list = []
#
# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
#
# Retrieve all of the anchor tags
# tags = soup('span')
# for tag in tags:
#Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('span', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    # acx = float(tag.contents[0])
    # list.append(acx)
# print(sum(list))
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# count: int= input('enter the count -')
# position: int = input('enter the postion -')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
# print(tags)
# for i in range(count):
#     print(tags[position].get('href', None))
# import urllib.request,urllib.parse,urllib.error
# from bs4 import BeautifulSoup
#
#
# url = input('Enter URL:')
# count = int(input('Enter count:'))
# position = int(input('Enter position:'))-1
# html = urllib.request.urlopen(url).read()
#
# soup = BeautifulSoup(html,"html.parser")
# href = soup('a')
#
# for i in range(count):
#     link = href[position].get('href', None)
#     print (href[position].contents[0])
#     html = urllib.request.urlopen(link).read()
#     soup = BeautifulSoup(html,"html.parser")
#     href = soup('a')

import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
url = input('enter the url :::')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
hre = soup('a')

for i in range(count):
    link = (hre[pos].get('href', None))
    print(hre[pos].contents[0])
    htl = urllib.request.urlopen(link).read()
    sou = BeautifulSoup(htl, "html.parser")
    hre = sou('a')