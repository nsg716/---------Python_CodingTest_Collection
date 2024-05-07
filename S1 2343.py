# 파라메트릭서치 : 최솟값, 최댓값을 알고 있으니 그 사이 범위에서 블루레이 크기를 가운데 값으로 잡고 사용 
N,M = map(int, input().split())
lessons = list(map(int,input().split()))
l = max(lessons)
r = sum(lessons)
m = (l+r) // 2
ans = r

def is_possible(sz):
    cnt = 1
    bluray = 0
    for lesson in lessons:
        if (bluray + lesson) <=sz:
            bluray+= lesson
        else :
            cnt += 1
            bluray = lesson
    return cnt <= M

while l <= r:
    if is_possible(m):
        ans = m
        r = m - 1
    else :
        l = m+1
    m = (l+r) // 2

print(ans)