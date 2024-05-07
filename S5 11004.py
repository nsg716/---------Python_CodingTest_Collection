#doit 파이썬 코테 준비 : 019번
# 퀵정렬 문제지만 굳이 그렇게 안풀어도 된다.

import sys 
input = sys.stdin.readline

N,K = map(int, input().split())
X = list(map(int, input().split()))
X.sort() # O(nlogn)
print(X[K-1])