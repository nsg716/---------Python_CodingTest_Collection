# doit 파이썬 코테 준비 : 058번
# 다익스트라 알고리즘 사용 + 사용한 노드를 방문리스트에 체크를 하고 다시 사용하지 않도록 한다. 
# K번째 최단 경로 찾기 

import sys
import heapq
input = sys.stdin.readline
N,M,K = map(int, input().split())
W = [[] for _ in range(N+1)]
distance= [[sys.maxsize] * K for _ in range(N+1)]


for _ in range(M):
    a,b,c = map(int, input().split())
    W[a].append((b,c))
    
pq = [(0,1)]
distance[1][0] = 0

while pq :
    cost, node = heapq.heappop(pq)
    for nNode, nCost in W[node]:
        sCost = cost + nCost
        if distance[nNode][K-1] > sCost:
            distance[nNode][K-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq,[sCost,nNode])
for i in range(1,N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K-1])