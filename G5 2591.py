# 숫자카드
# 다이나믹 프로그래밍

N = input() 

dp = [0] * (len(N))

dp[0] = 1

if len(N) >= 2 :
    if  N[1]!= '0' and N[0]+N[1] <='34':
        dp[1] = 2
    else:
        dp[1] = dp[0]


if len(N)>=3:
    for i in range(2, len(N)):
        # 두가지 다 가능한 경우
        if N[i-1]!='0' and N[i]!='0' and N[i-1]+N[i] <= '34':
            dp[i] = dp[i-1]+dp[i-2]
        # 이전이 0이거나 34 초과하는데 현재 숫자가 0이 아닌 경우 -> 독립으로 사용
        elif N[i] != '0':
            dp[i] = dp[i-1]
        # 현재 숫자가 0인 경우 -> 이어서 사용
        else:
            dp[i] = dp[i-2]


print(dp[len(N)-1])