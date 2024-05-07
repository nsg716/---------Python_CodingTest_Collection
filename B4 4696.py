while 1:
    
    a = float(input())
    if a == 0:
        break
    res = 0.0
    for i in range(5):
        res += a**i
    print(format (res,".2f"))