# N과 M (2)
# 백트래킹 
# 조합을 사용 

from itertools import combinations

N, M = map(int, input().split())

numList = [i for i in range(1, N+1)]
# [1, 2, 3, 4]

for seq in combinations(numList, M):
    print(*seq)