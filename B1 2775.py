import sys

N = int(sys.stdin.readline())

for i in range(N):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    x0 = list(a for a in range(1,b+1))
    
    for i in range(a):
        for j in range(1,b):
            x0[j] +=x0[j-1]
    print(x0[-1])