import sys

N = int(sys.stdin.readline())

x = []
for i in range(N):
    x.append(list(map(int, sys.stdin.readline().split())))

x.sort(key=lambda x:(x[1],x[0]))

for i in range(N):
    print(x[i][0], x[i][1])