# doit 파이썬 코테 준비 : 064번
# 최소 신장 트리 문제 : 그래프에서 모든 노드를 연결할 때 사용하는 에지들의 가중치의 합을 최소로 하는 트리 
# 사이클은 포함되지 않는다. N개의 노드가 있으면, 최소 신장 트리의 예지의 갯는 N-1개 이다. 
# 최소 스패닝 트리

from heapq import heappush, heappop
import sys 
input = sys.stdin.readline

def prim(start, weight):
    visit = [0] * (V + 1) # 정점 방문 처리
    q = [[weight, start]] # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    while cnt < V: # 간선의 개수 최대는 V-1
        k, v = heappop(q)
        if visit[v]: continue # 이미 방문한 정점이면 지나감
        visit[v] = 1 # 방문안했으면 방문처리
        ans += k # 해당 정점까지의 가중치를 더해줌
        cnt += 1 # 간선의 갯수 더해줌
        for u, w in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [w, u]) # 힙에 넣어줌
    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))

# 이 코드는 틀린 코드 런타임 오류 발생 
# import sys
# from queue import PriorityQueue

# input = sys.stdin.readline
# N,M = map(int,input().split())
# pq = PriorityQueue()
# parent = [0] * (N+1)

# for i in range(N+1):
#     parent[i] = i
    
# for i in range(M):
#     s,e,w = map(int, input().split())
#     pq.put((w,s,e))
    
# def find (a):
#     if a == parent[a]:
#         return a
#     else:
#         parent[a] = find(parent[a])
#         return parent[a]

# def union (a,b):
#     a = find(a)
#     b = find(b)
#     if a != b:
#         parent[b] = a
        
# useEdge = 0
# result = 0

# while useEdge < N-1:
#     w,s,e = pq.get()
#     if find(s) != find(e):
#         union(s,e)
#         result += w
#         useEdge += 1
        
# print(result)