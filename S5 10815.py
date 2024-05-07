# 배열보다 딕셔너리가 훨씬 빠르다 
import sys
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
y = list(map(int, sys.stdin.readline().split()))
con = {}

for i in range(N):
    con[x[i]] = 0
for i in range(M):
    if y[i] not in con:
        print(0, end= ' ')
    else:
        print(1, end= ' ') 
