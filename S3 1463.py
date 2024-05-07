#  6장 동적 계획법 
# Top-down재궈 vs bottom- up 반복문 
# DP는 좀화식을 어떻게 세워야 하는지 DP 테이블을 정하는 둥 감을 잡기 어렵다. DP 는 알고리즘 사이에서도 악명이 높다. 
# Top-down 
"""
import sys

sys.setrecursionlimit(10**6)
INF = 987654321 # 무한을 의미 
N = int(input())
cache = [INF] * (N+1)
cache[1] = 0
def dp(x):
    if cache[x] != INF:
        return cache[x]
    if x % 6  == 0:
        cache[x] = min(dp(x//3),dp(x//2))+1
    elif x%3 == 0:
        cache[x] = min(dp(x//3),dp(x-1))+1
    elif x%2 == 0:
        cache[x] = min(dp(x//2),dp(x-1))+1
    else :
            
        cache[x] = dp(x-1)+1
    return cache[x]

print(dp(N))

"""
"""
#  bottom- up
INF = 987654321 # 무한을 의미 
N = int(input())
dp = [INF] * (N+1)
dp[1] = 0
for i in range(2,N+1): 

    if i % 6  == 0:
        dp[i] = min(dp[i//3],dp[i//2])+1
    elif i%3 == 0:
        dp[i] = min(dp[i//3],dp[i-1])+1
    elif i%2 == 0:
        dp[i] = min(dp[i//2],dp[i-1])+1
    else :
        dp[i] =dp[i-1] +1

print(dp[N])
"""