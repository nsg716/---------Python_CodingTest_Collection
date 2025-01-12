#바이러스
from collections import deque
N = int(input())
M = int(input())
graph = [[]for i in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    x1, x2 = map(int, input().split())
    graph[x1] += [x2]
    graph[x2] += [x1]
    
# BFS 너비 우선 탐색     
visited[1] = 1
Q = deque([1])

while Q :
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1
            
print(sum(visited)-1) # 1은 빼기 

# # DFS 깊이 우선 탐색
# def DFS(v):
#     visited[v]= 1
#     for nx in graph[v]:
#         if visited[nx] ==0:
#             DFS(nx)
            
# DFS(1)
# print(sum(visited)-1)