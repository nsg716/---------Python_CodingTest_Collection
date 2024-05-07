import sys
N = int(sys.stdin.readline())

for _ in range(N):
    M = int(sys.stdin.readline())
    x = []
    
    for _ in range(M):
        x.append(int(sys.stdin.readline()))
    
    if M == 1:
        print(1)
    else :
        inn = 2
        while 1 :
            y = []
            for i in range(len(x)):
                y.append(x[i] % inn)
            a = set(y)
            a = list(a)
            if (len(x) == len(a)):
                print(inn)
                break
            else :
                inn+= 1            