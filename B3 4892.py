count = 1


while 1 :
    try :

        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0


        i = int(input())
        if (i == 0):
            break
        elif (i % 2 == 0):
            print("%d. even" %count , end = ' ')
        elif (i % 2 == 1) : 
            print("%d. odd" %count , end = ' ')
        n1 = 3*i
        if n1 % 2 == 0:
            n2 = n1 / 2 
        elif (n1 % 2 == 1):
            n2 = (n1+1)/2
        n3 = n2*3
        n4 = n3 //9
        print (int(n4))
        count += 1
        


    except :
        print("Error")
        break