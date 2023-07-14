fh=input("enter the file name")
try:
    fname=open(fh)
except:
    print("its a bad input you son of s bitch")
    quit()
x=fname.read()
y=x.upper()
z=y.strip()
print(z)
