# doit 파이썬 코테 준비 : 085번
# 동적 계획법 : 복잡한 문제를 여러개의 간단한 문제로 나누어서 계산을 하는 것으로 각각의 부분문제를 해결함으로써 최종적으로는 복잡한 문제의 답을 해결할 수 있는 방식
# 동적 계획법에는 톱-다운형식과 바텀-업 방식이 있다. 
# 점화식의 형태를 도출할 수 있어야 한다. 
# D[i] = D[i+1] / D[i] = MAX(D[i+1],D[i+T[i]] + P[i])

import sys 
input = sys.stdin.readline
N = int(input())
D = [0] * (N+2)
T = [0] * (N+1)
P = [0] * (N+1)

for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())


for i in range(N,0,-1):
    if i + T[i] > N+1:
        D[i] = D[i+1]
        
    else:
        D[i] = max(D[i+1], P[i]+ D[i + T[i]])

print(D[1])