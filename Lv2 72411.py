# 문제 6번 : 메뉴 리뉴얼 
# 순열 조합 문제 itertools.combination Counter 사용 

from collections import Counter
from itertools import combinations

def solution(orders, course):
    ans = []
    for n in course:
        menus = []
        for order in orders:
            menus += combinations(sorted(order),n)
        res = Counter(menus).most_common()
        for menu, cnt in res:
            if cnt >= 2 and cnt == res[0][1]:
                ans.append(''.join(menu))
    return sorted(ans)