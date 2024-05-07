# doit 파이썬 코테 준비 : 041번
# 오일러 피 함수 : P[N] 의 정의는 1부터 N까지 범위에서 N과 서로소인 자연수의 개수를 뜻한다. 
# 서로소의 개수룰 구하는 문제, P[i] = P[i] - P[i]/N(선택된 숫자) 를 반복 

import math 
N = int(input())
result = N

for p in range(2,int(math.sqrt(N)) + 1):
    if N % p == 0:
        result -= result / p
        while N % p == 0:
            N /=p
            
if N > 1:
    result -= result / N 
    
print(int(result))