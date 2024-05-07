while 1 :
    try : 
        m = int(input())
        if m == 0:
            break
        ml = (str(m))
        if ml == ml[::-1]:
            print("yes")
        else :
            print("no")
              
    except:
        print("error")
        break