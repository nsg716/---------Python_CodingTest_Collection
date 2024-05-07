a, b = map(int, input().split())
x = list(map(int, input().split()))

for i in range(5):
    print((x[i]-a*b), end = ' ')
