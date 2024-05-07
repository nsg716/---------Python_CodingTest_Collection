import sys

N = int(sys.stdin.readline())
x = [1,1]

for i in range(N):
    x.append(x[i] + x[i+1])

print((x[N]+x[N-1])*2)