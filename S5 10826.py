# 코테 2747이랑 같은 코드 

import sys

N = int(sys.stdin.readline())
x = [0,1]

for i in range(N):
    x.append(x[i] + x[i+1])

print(x[N])