# doit 파이썬 코테 준비 : 074번
# 조상 노드 구하기 문제 공통 조상이 누구인지 
# 이 문제는 시간 초과가 일어나므로 pypy3으로 해야한다. 

import sys 
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(0,N-1):
    s,e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
    
depth = [0]*(N+1)
parent = [0]*(N+1)
visited = [False] * (N+1)

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1
    now_size = 1
    count = 0
    while queue:
        now_node = queue.popleft()
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node
                depth[next] = level
        count += 1
        if count == now_size:
            count = 0
            now_size = len(queue)
            level += 1
BFS(1)

def executeLCA(a,b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp
        
    while depth[a] != depth[b]:
        a = parent[a]
        
    while a != b:
        a = parent[a]
        b = parent[b]
        
    return a

M = int(input())

for _ in range(M):
    a,b = map(int, input().split())
    print(str(executeLCA(a,b)))
    print("\n")    