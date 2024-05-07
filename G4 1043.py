# doit 파이썬 코테 준비 : 052번
# 유니온 파인드를 사용하여 문제를 해결 
# 3번째 줄부터 입력된 수 다음으로 진실을 아는 사람이 포함되어 있으면 그 파티에 있는 모든 사람이 아는 형식이다. 
# 거짓말을 할 수 있는 횟수 구하기 
N,M = map(int,input().split())
trueP = list(map(int, input().split()))
T = trueP[0]
del trueP[0]
result = 0
party = [[] for _ in range (M)]

def find (a):
    if a == parent[a]:
        return a
    else:
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

for i in range(M):
    party[i] = list(map(int,input().split()))
    del party[i][0]
    
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    firstPeople = party[i][0]
    for j in range(1,len(party[i])):
        union(firstPeople,party[i][j])
        
for i in range(M):
    isPossible = True
    firstPeople = party[i][0]
    for j in range(len(trueP)):
        if find(firstPeople) == find(trueP[j]):
            isPossible = False
            break
    if isPossible:
        result += 1
        
print(result)
        