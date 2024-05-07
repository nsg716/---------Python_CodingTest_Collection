# 우선순위 큐를 이용하여 문제를 푼 방법으로 첫번째 값은 무조건 중앙에 넣고, 비교하면서 트리를 만든다. 
# 힙은 시간복잡도는 O(logM)이며 이때 반복문을 돌기에 O(MlogM)이 된다. 이는 정렬보다 빠른 편이다.

import heapq

for _ in range(int(input())):
    M = int(input())
    ipt = []
    for _ in range((M //10) +1):
        for i in map(int, input().split()):
            ipt.append(i)

    ans = []
    max_hq = []
    min_hq = []

    def put(n):
        if max_hq and n >=-max_hq[0]:
            heapq.heappush(min_hq,n)
        else:
            heapq.heappush(max_hq,-n)
        
        if len(max_hq) > len(min_hq) +2 :
            heapq.heappush(min_hq, -heapq.heappop(max_hq))
        elif len(max_hq) < len(min_hq):
            heapq.heappush(max_hq, -heapq.heappop(min_hq))

    for i,val in enumerate(ipt):
        put(val)
        if i % 2 == 0:
            ans.append(-max_hq[0])

    print((M + 1) // 2)

    for i in range((len(ans) // 10) + 1):
        print(*ans[i*10:(i+1) * 10])