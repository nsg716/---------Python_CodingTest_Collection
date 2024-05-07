import sys

N = int(sys.stdin.readline())
x = [0]*10001
for i in range(N):
    a = (int(sys.stdin.readline()))
    x[a] = x[a]+1
    

for i in range(10001):
    if i !=0:
        for _ in range(x[i]):
            print(i)