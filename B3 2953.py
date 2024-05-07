x = list(0 for i in range(5))
for i in range(5):
    a, b, c, d = map(int, input().split())
    x[i] = a+b+c+d

print(int(x.index(max(x))+1), max(x))