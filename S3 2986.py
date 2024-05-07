# 수학의 마술사 
# 고려한 것 : 소수를 어떻게 구할 수 있는가 - 횟수를 어떻게 줄여하는가 시간복잡도를 줄이기 위해 많이 노력한 문제

import sys
N = int(sys.stdin.readline())

a= 0
 
for i in range(2,int((N**0.5)+1)):
    if N % i == 0:
        a = i
        a = int(N/a)-1
        break
print(N-a-1)

