N = 0
max = 0
for i in range(10):
    a, b = map(int, input().split())
    N -= a
    N += b
    if N > max:
        max = N
print(max)