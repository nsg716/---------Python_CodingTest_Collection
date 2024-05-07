while 1 :
    try : 
     a, b = map(int, input().split())
     
     if (a == 0 or b == 0 ) :
        break
     else :
        print(a+b)
    except :
        break 
