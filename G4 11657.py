# doit 파이썬 코테 준비 : 059번
# 벨만포드 알고리즘 : 알고리즘은 그래프에서 최단거리를 구하는 알고리즘으로 음수 사이클을 확인 가능하고 음수 가중치가 있어도 확인할 수 있다. 

import sys
input = sys.stdin.readline
N,M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N+1)

for i in range(M):
    start,end ,time = map(int, input().split())
    edges.append((start,end,time))
    
distance[1] = 0

for _ in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time
            
mCycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True
        
if not mCycle:
    for i in range(2,N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
            
else: 
    print(-1)