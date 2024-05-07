import math
a,b =map(int, (input().split()))
a = a-1
b= b-1
res= math.comb(a,b)
print(res)


# 순열 math.perm