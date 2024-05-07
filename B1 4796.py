count = 1
while True :
    
    a, b, c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0):
        break
    res = 0

    while (c-b>0):
        c-=b
        
        res += a

    if (c-b) ==0:
        pass
    if (a>=c) :
        res += c
    elif (a<c):
        res += a
    
    print("Case %d: %d" %(count,res))
    count += 1