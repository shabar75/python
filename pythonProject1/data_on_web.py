# #parsing xml
# import xml.etree.ElementTree as ET
# data = '''<person>
#           <name>shabar</name>
#           <phone type= "intl">9906894818</phone>
#           <email hide= "yes"/>
#           </person>'''
# tree = ET.fromstring(data)
# print('name:' , tree.find('name').text)
# print('phone no ha chu::', tree.find('phone').text)
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
#
# url = input('Enter url: ')
# print('Retrieving', url)
#
# total = 0
# count = 0
#
# uh = urllib.request.urlopen(url)
# data = uh.read()
# print('Retrieved', len(data), 'characters')
#
# tree = ET.fromstring(data)
# lst = tree.findall('comments/comment')
#
# for item in lst:
#     count = count + 1
#     t = item.find('count').text
#     # print(sum(t))
#     total = total + float(t)
#
# print('Count:', count)
# print('Sum:', total)











import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url = input('enter the url ::')
print('retriving::', url)
ul = urllib.request.urlopen(url)
data = ul.read()
print('retriving',len(data),'caharters')
lst= ET.fromstring(data)
tree = lst.findall('comments/comment')
count = 0
total = 0
for items in tree:
    count = count + 1
    print(items.find('name').text)
    t = items.find('count').text
    total = total + float(t)

print('count:',count)
print('sum:' ,total)
