x1 = []
x2 = []
sum1,sum2 = 0,0
for i in range(10):
    x1.append(int(input()))
for i in range(10):
    x2.append(int(input()))

x1.sort()
x2.sort()
for  i in range(3):
     sum1 += x1.pop()
     sum2 += x2.pop()
print(sum1,sum2)