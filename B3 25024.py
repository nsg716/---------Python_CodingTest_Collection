# 시간과 날짜
# 구현

N = int(input())

for i in range(N):
    res1, res2 = "No", "No"
    x, y = map(int, input().split())
    
    # 시간 유효성 검사
    if 0 <= x <= 23 and 0 <= y <= 59:
        res1 = "Yes"
    
    # 날짜 유효성 검사
    if 1 <= x <= 12:
        if x in (1, 3, 5, 7, 8, 10, 12):
            if 1 <= y <= 31:
                res2 = "Yes"
        elif x in (4, 6, 9, 11):
            if 1 <= y <= 30:
                res2 = "Yes"
        elif x == 2:
            if 1 <= y <= 29:
                res2 = "Yes"
    
    print(res1, res2)
