# doit 파이썬 코테 준비 : 094번
#  동적 계획법 톱- 다운 방식으로 해결한다. 
# 주석 처리된 부분은 시간초과되는 코드이다. 
"""
import sys 
input = sys.stdin.readline
N = int(input())
M = []
D = [[-1 for j in range(N+1)]for i in range(N+1)]

M.append((0,0))

for i in range(N):
    x,y = map(int, input().split())
    M.append((x,y))
    
def excute(s,e):
    result = sys.maxsize
    if D[s][e]  != -1:
        return D[s][e]
    if s == e:
        return 0
    if s+1 == e:
        return M[s][0] * M[s][1] *M[e][1]
    for i in range(s,e):
        result = min(result,M[s][0] * M[i][1] *M[e][1] + excute(s,i)  + excute(i+1,e))
        
    D[s][e] = result
    return D[s][e]

print(excute(1,N))
"""
import sys 
input = sys.stdin.readline
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr = [a for a, _ in arr] + [arr[-1][1]]
dp = [[0] * n for _ in range(n)]

for step in range(1,n):
    for loc in range(n-step):
        end = loc + step
        mul = arr[loc] * arr[end+1]
        minimum =  min(yk + xk + sz * mul for yk, xk, sz in zip(dp[loc][loc:end], dp[end][loc+1:end+1], arr[loc+1:end+1]))
        dp[loc][end] = dp[end][loc] = minimum

print(dp[0][-1])