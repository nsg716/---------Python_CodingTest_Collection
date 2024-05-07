# doit 파이썬 코테 준비 : 057번
# 다익스트라 알고리즘 사용

import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
M = int(input())
myList = [[] for _ in range(N+1)]
dist = [sys.maxsize] * (N+1) # 2의 64승 -1
visit = [False] * (N+1)

for _ in range(M):
    start, end, weight = map(int, input().split())
    myList[start].append((end, weight))
    
start_index, end_index = map(int, input().split())
def dijkstra(start,end):
    pq = PriorityQueue()
    pq.put((0,start))
    
    dist[start] = 0
    while pq.qsize() > 0:
        nowNode = pq.get()
        now = nowNode[1]
        if not visit[now]:
            visit[now] = True
            for n in myList[now]:
                if not visit[n[0]] and dist[n[0]] > dist[now] + n[1]:
                    dist[n[0]] = dist[now] + n[1]
                    pq.put((dist[n[0]],n[0]))
                    
    return dist[end]
print(dijkstra(start_index,end_index)) 