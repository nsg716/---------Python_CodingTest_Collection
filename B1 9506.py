
sum = 0
x = []

while 1 : 
    try : 
        n = int(input())
        if (n == -1):
            break
        for i in range(1,n-1):
            if (n % i == 0):
                x.append(i)
                sum += i
        if (sum == n):
            print ("%d = %d" %(n, x[0]), end = ' ')
            for i in (range(len(x)-1)):
                print("+ %d" %x[i+1], end = ' ')
            print()
        elif(sum != n) :
            print("%d is NOT perfect."  %n)
                
        sum = 0
        x = []
       
    except :
        break