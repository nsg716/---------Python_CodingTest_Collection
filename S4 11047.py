# doit 파이썬 코테 준비 : 032번
# 그리디 알고리즘 : 현재 상태에서 할 수 있는 가장 최선의 선택을 하는 알고리즘 
# 동적계획법 보다 구현하기 쉽다. 다만 항상 최적의 해를 보장하지는 않는다.
N,K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())
    
count = 0

for i in range(N - 1, -1, -1):
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]
        
print(count)