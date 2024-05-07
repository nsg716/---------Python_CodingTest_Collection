N = int(input())
x = []
y = []
for i in range(N):
    x.append(list(map(int, input().split())))
y = sorted(x)

for i in range(N):
    print(y[i][0], y[i][1])