# doit 파이썬 코테 준비 : 033번
# 우선순위 큐를 사용하여 작은 숫자를 먼저 계산하여 최소로 구현하는 문제.
from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    date = int(input())
    pq.put(date)
    
data1 = 0
date2 = 0
sum = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2 
    sum += temp
    pq.put(temp)
    
print(sum)
