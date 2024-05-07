
while 1 :
        x = list(map(int, input().split()))
        if (x[0] == 0 and x[1] == 0 and x[2] == 0):
             break
        y = sorted(x)
        x1 = y[0]**2+y[1]**2
        x2 = y[2]**2
        
        if x1 == x2:
            print("right")
        elif x1 != x2:
            print("wrong")
        
   