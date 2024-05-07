x = []
for i in range(8):
    x.append(int(input()))
res = 0
y = x
y = sorted(x)
cou = []
for i in range(5):
    res += y[i+3]
print(res)
for i in range(5):
    cou.append((x.index(y[i+3])+1))
cou.sort()
print(*cou)

