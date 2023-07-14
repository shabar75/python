text = "X-DSPAM-Confidence: 0.8475";
pos = text.find(':')
tex= text[pos+1:]
p = float(tex)
print(tex)