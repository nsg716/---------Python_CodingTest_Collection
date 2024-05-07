import math
a, b = map(int,input().split(":"))
a1 = a//math.gcd(a,b)
b2 = b//math.gcd(a,b)
print(a1,":",b2 , sep="")