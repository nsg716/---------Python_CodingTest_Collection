import sys 
sys.setrecursionlimit(10**6)# 재귀 횟수 늘림 
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    adj[a][b] = True # 무방향이므로 둘다 True
    adj[b][a] = True

ans = 0 # 방문 횟수 

check = [False] * (N+1)

def dfs(i):
    for j in range(1,N+1):
        if adj[i][j] and not check[j]: # 방문하지 않은 노드 발견시 체크를 한다.
            check[j] = True
            dfs(j) # 재귀, python 에서 재귀는 1000번이지만 횟수를 늘렸다 

for i in range(1,N+1):
    if not check[i]:
        ans+=1
        check[i] = True
        dfs(i)

print(ans) # 몇개의 연결요소가 있는지 확인 