# purse = dict()
# purse['candy'] = 12
# purse['chewg'] = 5
# purse['cig'] = 170
# print(purse)
# counts = dict()
# print('enter the line of text:')
# line = input('')
# words = line.split()
# print(words)
# print('counting......')
# for word in words:
#     counts[word]=counts.get(word, 0) + 1
#     print('conts', counts)




# counts = dict()
# lines = ('sha' , 'sha' , 'aaa')
# words = lines.split()
# print(words)
# for w in lines:
#     if w not in counts:
#         counts[w] =1
#     else:
#         counts[w] = counts[w] + 1
# print(counts)


# counts = dict()
# print('enter the lines')
# lines = input('')
# words = lines.split()
# print(words)
# for w in words:
#     if w in counts:
#         counts[w] = counts[w] + 1
#     else:
#         counts[w] = 1
# print(counts)
# counts = dict()
# print('enter the lines')
# lines = input('')
# words = lines.split()
# print(words)
# for w in words:
#     counts[w] = counts.get(w, 0) + 1
# print(counts)
fname = input('enter the file name')
if len(fname)<1: fname = 'shabar'
handle = open(fname)
di = dict()
for line in handle:
    line = line.rsplit()
    wds = line.split()
for w in wds:
    print(w)