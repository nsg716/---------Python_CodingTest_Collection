import sys

N = int(sys.stdin.readline())
x = []
for i in range(N):
    x.append(list(map(int, sys.stdin.readline().split())))

for i in x:
    count = 1
    for j in x:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
            
    print(count, end = " ")
        
    