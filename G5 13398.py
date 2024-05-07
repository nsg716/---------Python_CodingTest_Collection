# doit 파이썬 코테 준비 : 089번
# 왼쪽에서 비교했을 때 큰수 + 오른쪽에서 비교했을때 큰 수를 구하면 된다. 
# 정의 : D[N] : 0에서 N까지 길이에서 N을 포함하여 연속으로 수를 선택하여 구할 수 있는 최대 합 

N = int(input())
A = list(map(int, input().split()))

L = [0] * N 
L[0] = A[0]
result = L[0]

for i in range(1,N):
    L[i] = max(A[i],L[i-1]+A[i])
    result = max(result,L[i])
    
R = [0] * N 
R[N-1] = A[N-1]

for i in range(N-2,-1,-1):
    R[i] = max(A[i],R[i+1]+A[i])
    
for i in range(1,N-1):
    temp = L[i-1] + R[i+1]
    result = max(result,temp)

print(result)