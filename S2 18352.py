# doit 파이썬 코테 준비 : 046번
# 가중치가 없는 인접리스트를 이용하여 문제를 해결 
# BFS를 사용한다.
import sys
from collections import deque 
input = sys.stdin.readline

N,M,K,X= map(int, input().split())
A = [[] for _ in range(N+1)]
answer = []
visited = [-1] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue: 
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)
                
for _ in range(M):
    S,E = map(int, input().split())
    A[S].append(E)
    
BFS(X)

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)
        
if not answer:
    print(-1)
    
else :
    answer.sort()
    for i in answer:
        print(i)