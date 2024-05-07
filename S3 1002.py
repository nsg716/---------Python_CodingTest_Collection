import math
N = int(input())
for i in range(N):
    a1, b1, r1, a2, b2, r2 = map(int, input().split())
    s =  abs(r1+r2) # 두 원의 반지름의 합 
    dis = math.sqrt((a2-a1)**2 + (b2-b1)**2 )
    if (dis == 0 and r1 == r2):
        print(-1)
    elif abs (r1-r2) < dis < r1+r2:
        print(2)
    elif abs (r1-r2) == dis or dis == r1+r2:
        print(1)
    else : 
        print(0)
