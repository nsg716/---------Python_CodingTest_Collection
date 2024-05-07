import sys
# 첫 실버4 + 첫 스택 알고리즘 구현 + 알고리즘에 발이 다았음.
N = int(input())
x = []

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        x.append(int(command[1]))

    elif command[0] =='pop':
        if len(x) > 0 :
            print(x.pop())
        elif len(x) == 0:
            print("-1")

    elif command[0] == 'top':
        if len(x) > 0 :
             print(x[len(x)-1])
        elif len(x) == 0:
            print("-1")
       
   
    elif command[0] == 'empty':
        if len(x) > 0 :
             print("0")
        elif len(x) == 0:
            print("1")
    elif command[0] == 'size':
        print(len(x))
