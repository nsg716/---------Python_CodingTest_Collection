# doit 파이썬 코테 준비 : 061번
# 플로이드 - 워셜 : 최단거리 알고리즘 구하기 - 동적 계획볍의 원리를 이용해 알고리즘 접근 

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]

for i in range(1,N+1):
    distance[i][i] = 0
    
for i in range(M):
    s,e,v = map(int, input().split())
    if distance[s][e] > v :
        distance[s][e] = v
        
for k in range(1,N+1):
    for j in range(1,N+1):
        for i in range(1,N+1):
            distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j])
                
for i in range(1,N+1):
    for j in range(1,N+1):
        if distance[i][j] == sys.maxsize:
            print(0,end=' ')
        else:
            print(distance[i][j], end=' ')
    print()