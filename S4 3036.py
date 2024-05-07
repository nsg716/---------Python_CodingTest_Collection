import math
N = int(input())
x = list(input().split())

for i in range(1,len(x)):
    res = math.gcd(int(x[0]),int(x[i]))
    print(int(int(x[0])/res),"/",int(int(x[i])/res), sep="")