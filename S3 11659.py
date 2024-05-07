#doit 파이썬 코테 준비 : 003번
# 구간 합을 구하는 공식 
# i~J 까지의 구간 합 = S(j) - S(i-1)을 구하면 된다. 
# 이 방법이 알고리즘 측면에서 빠르다. 

import sys

N,M = map(int, sys.stdin.readline().split())

x = list(map(int,sys.stdin.readline().split()))
rsum = 0
y = [0]
for i in x:
    rsum += i
    y.append(rsum)

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    print(y[b] - y[a-1])