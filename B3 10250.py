N = int(input())

for i in range(N):
    r = 0 # 호실
    int1 = 0
    H = 0
    
    a ,b ,c = map(int, input().split())
    
    H = c%a # 층
    if c%a == 0:
        H = a

    int1 = c // a 
    r += int1
    
    if c%a != 0:
        r += 1
    print(H*100+r)