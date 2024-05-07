# 종료 시간을 기준으로 정렬 
# 종료시간이 더 빠른 순으로 결정 
# 2가지 방식 1. 시작시간과 종료시간이 같은 회의는 전부 고르는 전처리 방식  2. 종료시간이 같은 회의끼리는 시작시간으로 정렬한 뒤, 순서대로 고르는 방법 
"""
import sys

input = sys.stdin.readline

meetings = []

for _ in range(int(input())):
    start, end = map(int, input().split())
    meetings.append((end,start)) # 시작 시간을 끝에다가 둔다 

meetings.sort()  # 가장 낮은 순서대로 정렬
t , ans = 0 , 0
for end, start in meetings:
    if t <= start: # 종료시간이랑 시작시간이 같은 경우도 고려한다. 
        ans += 1
        t = end
print(ans)
"""
import sys

input = sys.stdin.readline

meetings = [tuple(map(int,input().split())) for _ in range(int(input()))]
meetings.sort(key=lambda x: (x[1], x[0]))

t , ans = 0 , 0
for start,end in meetings:
    if t <= start: # 종료시간이랑 시작시간이 같은 경우도 고려한다. 
        ans += 1
        t = end
print(ans)