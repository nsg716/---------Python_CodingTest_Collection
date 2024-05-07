# doit 파이썬 코테 준비 : 100번
# 결과값에 절댓값을 통하여 문제를 해결한다. 

import sys 
input = sys.stdin.readline
N = int(input())
x = []
y = []

for i in range(N):
    tempX,tempY = map(int, input().split())
    x.append(tempX)
    y.append(tempY)
    
x.append(x[0])
y.append(y[0])

result = 0

for i in range(N):
    result += (x[i] * y[i+1]) - (x[i+1] * y[i])
    
print(round(abs(result/2),1))
