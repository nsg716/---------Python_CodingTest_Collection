# doit 파이썬 코테 준비 : 086번
# 자릿수가 중요하다. 
# 2가지 형태로 나눌 수 있다. 0 으로 끝나는 이친수와 1로 끝나는 이친수가 있다. 

import sys
input = sys.stdin.readline
N = int(input())
D = [[0 for j in range(2)] for i in range(N+1)]

D[1][1] = 1
D[1][0] = 0

for i in range(2,N+1):
    D[i][0] = D[i-1][1] + D[i-1][0]
    D[i][1] = D[i-1][0]
    
print(D[N][0] +D[N][1])