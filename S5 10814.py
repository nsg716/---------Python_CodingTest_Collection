import sys
N = int(sys.stdin.readline())
x = []

for i in range(N):
    a, b = (map(str, sys.stdin.readline().split()))
    a = int(a)
    x.append((a, b))

x.sort(key=lambda x:x[0])

for i in range(N):
    print(x[i][0], x[i][1])