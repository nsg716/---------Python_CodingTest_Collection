# doit 파이썬 코테 준비 : 060번
# 벨만포드 알고리즘 : 알고리즘은 그래프에서 최단거리를 구하는 알고리즘으로 음수 사이클을 확인 가능하고 음수 가중치가 있어도 확인할 수 있다. 
# 업데이트 방향을 반대로 해야한다. 

import sys
input = sys.stdin.readline
N, sCity, eCity ,M = map(int, input().split())
edges = []
distance = [-sys.maxsize] * N

for _ in range(M):
    start,end, price = map(int, input().split())
    edges.append((start,end,price))
    
cityMoney = list(map(int, input().split()))

distance[sCity] = cityMoney[sCity]

for i in range(N+101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cityMoney[end] - price:
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= N-1:
                distance[end] = sys.maxsize
                
if distance[eCity] == -sys.maxsize:
    print("gg")
elif distance[eCity] == sys.maxsize:
    print("Gee")
else:
    print(distance[eCity]) 