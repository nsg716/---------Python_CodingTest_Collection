count = int(input())
x = list(map(int, input().split()))

y = x
max = 0
sum = 0
solv = 0

for i in range(count):
    if x[i]>max :
        max = x[i]

   
for i in range(count):
    y[i] = ((x[i] / max) * 100)

for i in range(count):
    sum += y[i]
solv = sum / count
print(solv)
