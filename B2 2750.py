N = int (input())
x = []
for i in range(N):
    x.append(int(input()))

x.sort()
for i in range(N):
    print(x[i])