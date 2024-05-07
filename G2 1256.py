# 모든 경우의 수를 구하면 10^58이다. 다이나믹 프로그래밍으로 풀면 O(NM)이다.
N,M,K =  map(int, input().split())
dp = [[0] * (M+1) for _ in range(N+1)]
for j in range(1,M+1):
    dp[0][j] = 1

for i in range(1,N+1):
    dp[i][0] = 1
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

def s(n,m,k):
    if n == 0:
        print('z' * m)
        return 
    elif m == 0:
        print('a' * n)
        return 
    
    if dp[n-1][m] >= k:
        print('a', end='')
        s(n-1,m,k)
    else:
        print('z',end='')
        s(n,m - 1 , k - dp[n-1][m])

if dp[N][M] < K:
    print(-1)
else: 
    s(N,M,K)