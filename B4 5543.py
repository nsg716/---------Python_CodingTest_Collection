x = []
y = []
for i in range(3):
    x.append(int(input()))
for i in range(2):
    y.append(int(input()))

a = min(x)
b = min(y)
print(a+b-50)