# doit 파이썬 코테 준비 : 080번
# 조합으로 문제 풀기 : 확률 문제 

D = [0] * 51
probability = [0] * 51
M = int(input())
D = list(map(int, input().split()))
T = 0

for i in range(0,M):
    T += D[i]
    
K = int(input())
ans = 0
for i in range(0,M):
    if D[i] >= K :
        probability[i] = 1
        for k in range(0,K):
            probability[i] = probability[i] *(D[i] - k ) / (T-k)
        ans += probability[i]
        
print(ans)
             