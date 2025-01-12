# 1, 2, 3 더하기
# a[n] = a[n-1]+ a[n-2]+a[n-3] 점화식
import sys 
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    S = int(input())
    dp = [0] * (S+1)
    
    for i in range(1, S+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2 # 1+1,2
        elif i == 3:
            dp[i] = 4 # 1+1+1,1+2,2+1,3
        else:
            dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]
   
    print(dp[S])
            
