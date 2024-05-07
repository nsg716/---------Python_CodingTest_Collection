"""
# 스텍으로 푸는 방법
for _ in range(int(input())):
    stk1 = []
    stk2 = [] # t
    for ch in input(): # ch 가 들어 올때, 검사를 한다. 
        if ch == '<':
            if len(stk1): # 리스트 안에 들어있으면 작동 
                stk2.append(stk1.pop()) # 가장 마지막에 들어온 append를 pop한다. 이는 들어온 순서대로 reverse하기 위한 리스트로 보내진다. 
        elif ch == '>':
            if len(stk2):
                stk1.append(stk2.pop())
        elif ch == '-':
            if len(stk1):
                stk1.pop()
        else :
            stk1.append(ch)
    print(''.join(stk1) + ''.join(reversed(stk2))) # 여기가 핵심이다 .뒤집힌 문자열을 출력하여 <>의 표시를 살린다. 

"""
from collections import deque

for _ in range(int(input())):
    dq1 = deque()
    dq2 = deque()
    for ch in input():
        if ch == '<':
            if len(dq1):
                dq2.appendleft(dq1.pop()) # 덱큐에만 있는 특징 왼쪽 삽입이다. 
        elif ch == '>':
            if len(dq2):
                dq1.append(dq2.popleft()) # 덱큐에만 있는 특징 왼쪽 삭제 (삭제 이후 리턴)
        elif ch == '-':
            if len(dq1):
                dq1.pop()
        else:
            dq1.append(ch)
        
    print(''.join(dq1) + ''.join(dq2))