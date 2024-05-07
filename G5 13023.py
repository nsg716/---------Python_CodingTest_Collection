# doit 파이썬 코테 준비 : 025번
# DFS로 풀이 , 재귀와 형식이 비슷하다. 
# 문제에서DFS를이용하는 만큼 깊이우선탐색과 넓이 우선 탐색을 잘 알아두어야 한다.

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int, input().split())
arrive = False 
A = [[] for _ in range(N + 1)]

visited = [False] * (N+1)

def DFS (now,depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True 
    for i in A[now]:
        if not visited[i]:
            DFS(i,depth+1)
    visited[now] = False
    
for _ in range(M):
    s,e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
    
for i in range(M):
    DFS(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
        