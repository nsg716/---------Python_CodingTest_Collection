import sys
N = int(sys.stdin.readline())
x =[]
count =1
for i in range(N):
    x.append(int(sys.stdin.readline()))
max = x[-1]

for i in reversed(range(N)):
    if (x[i]>max):
        max = x[i]
        count += 1
        
print(count)