N = int(input())

while 1:
    M = int(input())
    if M == 0:
        break
    
    if M % N ==  0:
        print("%d is a multiple of %d." %(M,N) )
    else :
        print("%d is NOT a multiple of %d." %(M,N)) 
