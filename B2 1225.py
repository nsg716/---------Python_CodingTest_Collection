
import sys
a, b = map(str, sys.stdin.readline().split())
x = []
y = []
sum1 = 0
for i in range(len(a)):
    x.append(int(a[i]))
for j in range(len(b)):
    y.append(int(b[j]))

res1,res2 = 0,0
res1 = sum(x)
res2 = sum(y)
print(res1*res2)