# doit 파이썬 코테 준비 : 071번
# 세그먼트 트리 : 구간합을 빠르게 하기 위해 고안한 자료구조 코딩 테스트 영역에서는 큰 차이 없다. 
# 힙으로 문제를 해결할 수 있으나 데이터 갱신에 있어서 시간이 오래 걸리므로 문제를 보다 빠르게 풀기 위해서 세그먼트 트리를 사용한다. 

import sys
input = sys.stdin.readline
N,M,K = map(int, input().split())
treeHeight = 0 
length = N

while length != 0:
    length //= 2
    treeHeight += 1
    
treeSize = pow(2,(treeHeight + 1))
letfNodeStartIndex = treeSize // 2-1
tree = [0] * (treeSize + 1)

for i in range(letfNodeStartIndex + 1, letfNodeStartIndex + N + 1):
    tree[i] = int(input())
    
def setTree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1
        
setTree(treeSize - 1)

def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2
        
def getSum(s,e):
    partSum = 0
    while s <= e : 
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
            
        s = s // 2 
        e = e // 2
        
    return partSum

for _ in range(M+K):
    qusetion ,s,e = map(int, input().split())
    if qusetion == 1:
        changeVal(letfNodeStartIndex+ s, e)
    elif qusetion == 2:
        s = s + letfNodeStartIndex
        e = e + letfNodeStartIndex
        print(getSum(s,e))