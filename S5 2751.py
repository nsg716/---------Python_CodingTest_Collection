import sys

N = int(sys.stdin.readline())
x =[]
for i in range(N):
    x.append(int(sys.stdin.readline()))
y = sorted(x)
for i in range(N):
    print(y[i])