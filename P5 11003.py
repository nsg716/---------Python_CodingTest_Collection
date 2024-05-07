#doit 파이썬 코테 준비 : 010번
#시간에 압박이 심하기에 라이브러리 사용 # 슬라이싱 윈도우 전략 사용 
# 정렬 알고리즘은 사용 불가 

from collections import deque
N,L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

# 새로운 값이 들어오면 정렬 대신 현재 수보다 큰 값을 덱에서 제거 
for i in range(N):
    while mydeque and mydeque[-1][0]> now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i-L:
        mydeque.popleft()
    print(mydeque[0][0], end=" ")