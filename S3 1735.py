import math
a1, b1 =map(int, input().split())
a2, b2 =map(int, input().split())
res1 = (a1*b2)+(a2*b1)
res2  = (b1*b2)
res = math.gcd(res1, res2)
print(int(res1/res),int(res2/res))