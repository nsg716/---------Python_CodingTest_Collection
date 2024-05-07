# doit 파이썬 코테 준비 : 050번
# 이문제는 집합을 표현하는 함수를 적절히 만들 수 있는지 묻는 문제이다. 
# 해결 방법은 유니온 파인드를 사용하여 경로를 압축하여 문제를 해결한다. 
# 유니온 파인드는 union, find를 이용하여 index와 value를 비교하여 문제를 해결합니다. 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N,M = map(int, input().split())
parent = [0]* (N+1)

def find (a):
    if a == parent[a]:
        return a
    else :
        parent[a] = find(parent[a])
        return parent[a]
def union (a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(0,N+1):
    parent[i] = i
    
for i in range(M):
    question, a,b = map(int, input().split())
    if question == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print("YES")
        else:
            print("NO")