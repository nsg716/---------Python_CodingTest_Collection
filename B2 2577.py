
a = int(input())
b = int(input())
c = int(input())
num = a * b * c
x = list(0 for i in range(10))
snum = str(num)
for i in range(10):
    x[i] = snum.count(str(i))

for i in range(10):
    print(x[i])