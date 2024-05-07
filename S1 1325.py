# doit 파이썬 코테 준비 : 047번
# 시간복잡도의 제한이 크지 않기에 알고리즘 구현에 신경을 써야 하는 문제이다. 여기서 인접리스트를 이용하여 문제를 해결했다. 
# python코드는 BFS의 공간을 많이 사용하고, 시간 초과가 일어난다 그래서 pypy로 실행을 함. 
import sys
from collections import deque 
input = sys.stdin.readline
N,M = map(int, input().split())
A = [[] for _ in range(N+1)]
answer = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    A[b].append(a)

# bfs
ans = []
for i in range(1, N+1):
    visited = [False]*(N+1)
    queue = deque([i])
    visited[i] = True
    
    cnt = 1
    while queue:
        x = queue.popleft()
        for j in A[x]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)
                cnt += 1
    ans.append(cnt)

max_cnt = max(ans)
for i in range(N):
    if ans[i] == max_cnt:
        print(i+1, end=" ")
                
                         