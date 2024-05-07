# doit 파이썬 코테 준비 : 073번
# 기본 틀은 세그먼트 트리이지만 코드의 수정을 할 수 있는 훈련이 있어야 한다. 

import sys 
input = sys.stdin.readline

N,M,K = map(int, input().split())
treeHeight = 0
length = N
MOD = 1000000007


while length != 0:
    length //= 2
    treeHeight += 1
    
treeSize = pow(2,(treeHeight + 1))
letfNodeStartIndex = treeSize // 2-1
tree = [1] * (treeSize + 1)


for i in range(letfNodeStartIndex+1 , letfNodeStartIndex + N + 1):
    tree[i] = int(input())


    
def setTree(i):
    while i != 1:
        tree[i//2] = tree[i//2] * tree[i] % MOD
        i -= 1
        
setTree(treeSize - 1)

def changeVal(index, value):
    tree[index] = value
    while index > 1:
        index = index // 2
        tree[index] = tree[index*2] % MOD * tree[index * 2 + 1] % MOD
        
def getMul(s,e):
    partMul = 1
    while s <= e:
        if s % 2 == 1:
            partMul = partMul * tree[s]%MOD
            s += 1
        if e %2 == 0:
            partMul = partMul * tree[e] % MOD
            e -= 1
        s = s // 2
        e = e // 2
        
    return partMul

for _ in range(M+K):
    question , s,e = map(int, input().split())
    if question == 1:
        changeVal(letfNodeStartIndex+s,e)
    elif question == 2:
        s = s+ letfNodeStartIndex
        e = e + letfNodeStartIndex
        print(getMul(s,e))