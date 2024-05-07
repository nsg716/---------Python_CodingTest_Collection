import sys
N = int(sys.stdin.readline())
co = int(sys.stdin.readline())
x = []
count =0
for i in range(N-1):
    x.append(int(sys.stdin.readline()))
x.sort()
x.reverse()
if (N == 1):
    print(0)
else :
    while x[0] >= co:
        co += 1
        x[0] -=1
        count += 1
        x.sort()
        x.reverse           
    print(count)