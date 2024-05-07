# doit 파이썬 코테 준비 : 038번
# [A,B] 범위에 있는 소수의 제곱의 개수 구하기
# 에라토스테네스의 체를 이용 : 어떤 수 까지 소수를 구하는 거면 그 수의 제곱근 + 1 을 하여 배수를 지우는 방식 

import math 
Min,Max = map(int,input().split())

A =[0] * (10000001)


for i in range(2,len(A)):
    A[i] = i
for  i in range(2,int(math.sqrt(len(A))+1)):
    if A[i] == 0:
        continue
    # 배수 지우기 
    for j in range(i + i, len(A), i):
        A[j] = 0
        
count = 0

for i in range(2,10000001):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= Max / temp:
            if A[i] >= Min / temp:
                count += 1
            temp = temp *A[i]
            
print(count)
                     
    