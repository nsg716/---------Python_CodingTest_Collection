#doit 파이썬 코테 준비 : 024번
# DFS 깊이 우선 탐색 , 재귀형태를 띄고 있다. 
# 소수 판별에는 "" 에라토스테네스의 체를 사용"" 다만 여기서는 단순한 소수 판별 함수를 사용 

import sys
sys.setrecursionlimit(100000) # 재귀 횟수 설정
input = sys.stdin.readline
N = int(input())

def isPrime(num):
    for i in range(2,int(num / 2 + 1)):
        if num % i == 0:
            return False #소수가 아닌 경우 
    return True

def DFS(number):
    if len(str(number)) == N:
        print(number)
    else: 
        for i in range(1,10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)
                
# 일의 자리 
DFS(2)
DFS(3)
DFS(5)
DFS(7)
