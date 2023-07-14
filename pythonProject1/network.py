# urllib
import urllib.request, urllib.error

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in handle:
    words= line.decode().strip()
    for word in words:
        count[word]=count.get(word, 0) +1
print(count)
