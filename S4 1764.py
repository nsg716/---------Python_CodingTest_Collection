# 듣보잡
import sys 


N,M = map(int,input().split())

x1 = set()
x2 = set()
y = []
for i in range(N):
    x1.add(input())
for i in range(M):
    x2.add(input())

y = sorted(list(x1 & x2))



print(len(y))
for i in y:
    print(i)
