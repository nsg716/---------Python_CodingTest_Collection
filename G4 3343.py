import sys
import math
total, f1, v1, f2, v2 = map(int, sys.stdin.readline().rstrip().split())
count = 0
res = float('inf')
if v1*f2 < v2*f1:
    f1,v1,f2,v2 = f2,v2,f1,v1 # 기존 코드에서 가성비 비교를 하지 않는다 즉 실행시간을 줄인다.
for i in range(f2): # 기존 코드는 실행시간이 n임에 반해서 이것을 상수값이다.
    j = math.ceil((total-i*f1)/f2)
    a = False
    if  j < 0:
        j = 0
        a = True
    res = min(res, i*v1+j*v2)
    if a:
        break

print(res)

"""
sl1 =  f1/v1
sl2 = f2/v2
if (sl1>sl2):
    while (total > f1):
        total -= f1
        count += 1
        b= v1
else :
    while (total > f2):
        total -= f2
        count += 1
        b= v2

res = count*b

if ((total-f1) <=0) and v1<v2:
    res+= v1
elif ((total-f2) <=0) and v1>v2:
    res += v2
print(res)

""" 