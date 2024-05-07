
N = int(input())
x = []
res = []
for i in range(N):
    x.append(int(input()))

x = sorted(x,reverse=True)
for i in range(1,N+1):
    res.append(x[i-1]*i)
    N-=1

print(max(res))