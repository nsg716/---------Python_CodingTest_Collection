# doit 파이썬 코테 준비 : 069번
# 문자열 집합 구하기  
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
textList = set([input() for _ in range(N)])
result = 0


for _ in range(M):
    word = input()
    if word in textList:
        result += 1
        
print(result)
    