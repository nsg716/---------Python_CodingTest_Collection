#doit 파이썬 코테 준비 : 007번
# 투 포인터 문제, O(nlogn)로도 풀 수 있다.
import sys 

input = sys.stdin.readline 

N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0 
i = 0
j = N -1

while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i+= 1
        j -= 1
print(count)