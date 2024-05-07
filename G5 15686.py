# 완전탐색이 편하다 길찾기 방식을 너비/깊이 우선탐색으로 찾아도 되지만 최대 경우의 수는 1,201,200이므로 1초내 끝낼수 있다.
# 시간복잡도 : H 집수, C : 치킨집수 O(2^C *H*C)

from itertools  import  combinations

N,M = map(int, input().split())
houses = []
chickens = []
for i in range(N): 
    for j, val in enumerate(map(int,input().split())): # 열거하다 
        if val == 1:
            houses.append((i,j))
        elif val == 2:
            chickens.append((i,j))

def get_dist(cord1, cord2):
    r1,c1 = cord1
    r2,c2 = cord2
    return abs(r1-r2) + abs(c1-c2)

ans = 2 * N * len(houses)

for comb in combinations(chickens,M):# 조합 사용 완전 탐색의 가장 중요한 부분, 모든 경우의 수를알려준다. 
    tot = 0 
    for house in houses:
        tot += min(get_dist(house, chicken) for chicken in comb)

    ans =  min(ans, tot)

print(ans)

