#doit 파이썬 코테 준비 : 005번
# 정해진 구간에서 정해진 수로 나누었을 때 나누어 떨어지는 수
# 나머지가 0 이 아닌 수는 빼는 경우의 수도 있다.
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
result = 0

for i in range(1,n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    r = S[i] % m
    if r == 0:
        result += 1
    C[r] += 1
    
for i in range(m):
    if C[i] > 1:
        result += (C[i] * (C[i]-1) //2)
print(result)