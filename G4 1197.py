# doit 파이썬 코테 준비 : 064번
# 최소 신장 트리 문제 : 그래프에서 모든 노드를 연결할 때 사용하는 에지들의 가중치의 합을 최소로 하는 트리 
# 사이클은 포함되지 않는다. N개의 노드가 있으면, 최소 신장 트리의 예지의 갯는 N-1개 이다. 

import sys
from queue import PriorityQueue

input = sys.stdin.readline
N,M = map(int,input().split())
pq = PriorityQueue()
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i
    
for i in range(M):
    s,e,w = map(int, input().split())
    pq.put((w,s,e))
    
def find (a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union (a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
useEdge = 0
result = 0

while useEdge < N-1:
    w,s,e = pq.get()
    if find(s) != find(e):
        union(s,e)
        result += w
        useEdge += 1
        
print(result)