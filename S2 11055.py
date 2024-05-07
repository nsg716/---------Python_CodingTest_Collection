# 최장 증가 부분 수열 

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = A[0]
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max (dp[i],dp[j])
    dp[i]+=A[i]

print(max(dp))