# 복기를 하니 찾은 파이썬 함수

import sys
a, b = map(int, sys.stdin.readline().split())
result = 1
result2 = 1
for i in range(a,a-b,-1):
    result*= i
    
for i in range(1,b+1):
    result2 *=i

result = int(result//result2)%10007
print(result)