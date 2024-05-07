a, b = map(int,input().split())
b = b*(1/100)

c = a*b
a = a-c

if (a>=100):
    print("0")
else :
    print("1")