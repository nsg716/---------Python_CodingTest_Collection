# doit 파이썬 코테 준비 : 056번
# 다익스트라 알고리즘 : 최단거리 구하기 알고리즘 
# 방문을 하지 않은 노드중에 작은 노드를 구한다. 

import sys
input = sys.stdin.readline
from queue import PriorityQueue

V,E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V+1) # 2의 64승 -1
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u,v,w = map(int, input().split())
    myList[u].append((v,w))
    
q.put((0,K))
distance[K] = 0 

while q.qsize() > 0:
    currnet = q.get()
    c_v = currnet[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next],next))
            
for i in range(1,V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")