import sys
# 첫 큐 알고리즘 구현 
N = int(input())
x = []

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        x.append(int(command[1]))

    elif command[0] =='pop':
        if len(x) > 0 :
            print(x.pop(0))
        elif len(x) == 0:
            print("-1")

    elif command[0] == 'empty':
        if len(x) > 0 :
             print("0")
        elif len(x) == 0:
            print("1")
    elif command[0] == 'size':
        print(len(x))

    elif command[0] == 'front':
        if len(x)>0:
            print(x[0])
        elif len(x) == 0:
            print("-1")
    elif command[0] == 'back':
        if len(x)>0:
            print(x[-1])
        elif len(x) == 0:
            print("-1")