N = int(input())
x = list(map(int, input().split()))
y = []
for i in range(N):
    y.insert(x[i],i+1)
y.reverse()
print(*y)