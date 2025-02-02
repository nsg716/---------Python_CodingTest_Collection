# doit 파이썬 코테 준비 : 054번
# 위상 정렬은 한뒤 그 값들을 더해서 결과를 출력하면 되는 문제.
# 위상정렬 문제 : 사이클이 없는 방향그래프에서 노드 순서를 찾는 알고리즘 

from collections import deque
N = int(input())
A = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
selfBuild = [0] * (N+1)

for i in range(1,N+1):
    inputlist = list(map(int, input().split()))
    selfBuild[i] =(inputlist[0])
    index = 1
    while True:
        preTemp = inputlist[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1
        
queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
result = [0] * (N+1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        
        result[next] = max(result[next],result[now] + selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)
            
for i in range(1,N+1):
    print(result[i] + selfBuild[i])
    