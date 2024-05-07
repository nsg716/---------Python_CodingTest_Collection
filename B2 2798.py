N, M = map (int, input().split())
xx = 0
x = list(map (int, input().split()))
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if x[i] + x[j] + x[k] > M:
                continue
            else:
                 xx = (max(xx, x[i] + x[j] + x[k]))
print(xx)