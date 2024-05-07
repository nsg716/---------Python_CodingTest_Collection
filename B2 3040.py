from itertools import combinations # 조합 선언

for i in combinations([int(input()) for _ in range(9)], 7): # 9C7 조합 36개 이므로 완전 탐색으로 찾는다. 
    if sum (i) == 100:
        for j in sorted(i):
            print(j)
        break