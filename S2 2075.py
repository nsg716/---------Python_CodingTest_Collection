import heapq

hq = []
N = int(input())
for _ in range(N): # 큐의 크기
    for i in map(int, input().split()):
        if len(hq) >=N: # 우선순위큐의 크기가 N보다 작을 때는 입력값을 push한다.N보다 크면 가장 작은 값을 pop한다.
            heapq.heappushpop(hq,i)
        else:
            heapq.heappush(hq,i)
print(heapq.heappop(hq))