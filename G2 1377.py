#doit 파이썬 코테 준비 : 016번
# 버블 정렬인데 실제로 구현을 하면 시간이 오래 걸린다. 따라서 정렬전 위치와 정렬 후 위치를 비교하여 가장 많이 이동한 값을 찾으면 된다.

import sys 
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()),i))
    
Max = 0
sort_A = sorted(A) # 정렬 전 배열과 정렬 후 배열을 비교하기 위해 남긴다.

for i in range(N):
    if Max < sort_A[i][1] - i :
        Max = sort_A[i][1] - i
print(Max + 1) # swap이 일어나지 안았을 때 반복문 실행을 염두하여 + 1을 한다.