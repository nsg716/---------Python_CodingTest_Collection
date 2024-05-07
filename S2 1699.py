# 점화식 : f(i) = min ((f(i-1^2),(f(i-2^2),(f(i-3^2),...,(f(i-j^2))(i>= j^2)
# 다이나믹 프로그래밍 bottom -up

N = int(input())
dp = [i for i in range(N+1)]
for i in range(4,N+1):
    for j in range(1,i):
        if i < j *j:
            break

        if dp[i] > dp[i - j*j] + 1:
           dp[i] = dp[i - j*j] + 1

print(dp[N])
# 그리디 알고리즘으로는 풀 수 없다. 반례가 존재하기 때문에 