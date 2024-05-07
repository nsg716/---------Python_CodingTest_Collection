# doit 파이썬 코테 준비 : 072번
# 전형적인 세그먼트 트리 문제 
# 구간이 주어짐에 따라 그에 맞는 최솟값을 구해야한다.
import sys 
input = sys.stdin.readline

N,M = map(int, input().split())
treeHeight = 0
length = N

while length != 0:
    length //= 2
    treeHeight += 1
    
treeSize = pow(2,(treeHeight + 1))
letfNodeStartIndex = treeSize // 2-1
tree = [sys.maxsize] * (treeSize + 1)

for i in range(letfNodeStartIndex+1 , letfNodeStartIndex + N + 1):
    tree[i] = int(input())
    
    
def setTree(i):
    while i != 1:
        if tree[i // 2] > tree[i]:
            tree[i // 2] = tree[i]
        i -= 1
        
setTree(treeSize - 1)

def getMin(s,e):
        Min = sys.maxsize
        while s <= e:
            if s % 2 == 1:
                Min = min(Min,tree[s])
                s += 1
            if e % 2 == 0:
                Min = min(Min,tree[e])
                e -= 1
            s = s // 2
            e = e // 2
            
        return Min 
    
for _ in range(M):
    s,e = map(int, input().split())
    s = s + letfNodeStartIndex
    e = e + letfNodeStartIndex
    print(getMin(s,e))