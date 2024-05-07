# python3은 시간초과가 뜨므로 pypy로 진행
#브루트포스 알고리즘 문제

import sys

N, M, B = map(int, sys.stdin.readline().split())
x = []
for _ in range(N):
    x.extend(map(int, sys.stdin.readline().split()))
        
time = [0 for i in range(257)]
height = 0 
for g in range(257):
    block = B
    for i in x:
        if i <= g: # i == g이면 g-i=0
            time[g] += g - i
            block -= g - i
        else:
            time[g] += 2 * (i - g)
            block += i - g
    if block >= 0 and time[g] <= time[height]: # 오름차순으로 순회하므로, 답이 여러 개 있을 때 그중에서 땅의 높이가 가장 높은 것을 저장하게 됨
        height = g 

print(time[height], height)