# doit 파이썬 코테 준비 : 062번
# 플로이드 워셜 알고리즘 
N = int(input())
distance = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    distance[i] = list(map(int,input().split()))
    
for k in range(N):
    for j in range(N):
        for i in range(N):
            if distance[i][k] == 1 and distance[k][j] == 1:
                distance[i][j] = 1
                
for i in range(N):
    for j in range(N):
        print(distance[i][j],end=' ')
    print()