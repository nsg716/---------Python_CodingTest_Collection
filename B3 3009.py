x1= []
y1= []
result = []
for i in range(3):
    a, b= (map(int, input().split()))
    x1.append(a)
    y1.append(b)

for i in range(len(x1)):
    if x1.count(x1[i]) == 1:
        result.append(x1[i])
for i in range(len(y1)):
    if y1.count(y1[i]) == 1:
        result.append(y1[i])

print(*result)