# import re
# hand = open("abc.txt", "r")
# numlist = []
#
# for line in hand:
#     line = line.rstrip()
#     extract = re.findall('[0-9]+', line)
#
#     if len(extract) < 1 : continue
#
#     for i in range(len(extract)):
#         num = float(extract[i])
#         numlist.append(num)
#
# print(sum(numlist))











# import re
# handle = open("abc.txt", "r")
# numlist = []
# for line in handle:
#     line.rstrip()
#     y= re.findall('[0-9]+', line)
#     if len(y)<1:continue
#
#     for i in range(len(y)):
#         num = float(y[i])
#         numlist.append(num)
#
# print(sum(numlist))

import re
hand = open("abc.txt", "r")
list =[]
for line in hand:
    line.rstrip()
    y = re.findall('[0-9]+', line)
    if len(y)<1: continue
    for i in range(len(y)):
        num = float(y[i])
        list.append(num)
print(sum(list))





