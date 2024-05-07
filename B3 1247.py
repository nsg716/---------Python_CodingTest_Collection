import sys
for i in range(3):
    N = int(sys.stdin.readline())
    sum = 0
    for i in range(N):
        s = int(sys.stdin.readline())
        
        sum += s
    if sum == 0:
        print(0)
    elif sum > 0:
        print("+")
    else :
        print("-")