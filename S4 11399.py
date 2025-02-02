#doit 파이썬 코테 준비 : 018번
# 삽입 정렬
# 그리디 방식 : 가장 짧은 시간이 걸리는 사람을 앞으로 정렬하는 것

N = int(input())
A = list(map(int, input().split()))
S = [0]*N

for i in range(1,N): # 삽입 정렬
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+ 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point,-1):
        A[j] = A[j-1]
        
    A[insert_point] = insert_value
    
S[0] = A[0]
sum = 0
for i in range(1,N):
    S[i] = S[i-1] +A[i] 
for i in range(0,N):
    sum += S[i]
print(sum)    


