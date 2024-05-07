# doit 파이썬 코테 준비 : 048번
# 이분그래프란 : 각 집합에 속한 노드끼리 서로 인접하지 않는 두 집합으로 그래프의 노드를 나눌 수 있을 때의 그래프를 의미 
# 출발 노드와 도착 노드의 집합이 같으므로 이분 그래프 불가능 


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
IsEven = True 

def DFS(node):
    global IsEven
    visited[node] = True 
    for i in A[node]:
        if not visited[i]:
            check[i] = (check[node] + 1) % 2
            DFS(i)
            
        elif check[node] == check[i]:
            IsEven = False
            
for _ in range(N):
    V,E = map(int, input().split())
    A = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V+1)
    IsEven = True
    
    for i in range(E):
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start)
    
    for i in range(1,V+1):
        if IsEven:
            DFS(i)
        else:
            break

    if IsEven:
        print("YES")
    else:
        print("NO")