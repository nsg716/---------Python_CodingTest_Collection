# doit 파이썬 코테 준비 : 053번
# 위상정렬 문제 : 사이클이 없는 방향그래프에서 노드 순서를 찾는 알고리즘 
# 이 문제는 답이 여러가지인 경우 아무거나 출력한다 -> 예시 2번 보기 정답이 아니지만 정답 코드이다. 
from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    S,E = map(int, input().split())
    A[S].append(E)
    indegree[E] += 1
    
queue = deque()

for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)
        
while queue:
    now = queue.popleft()
    print(now, end=' ')
    for next in A[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)