import sys

N = int(sys.stdin.readline())


for i in range(N):
    val1 = [0,1]
    a =  int(sys.stdin.readline())
    if a == 0:
       
        print(1, 0)
    elif a==1 :
       
        print (0, 1)
    else :
        for i in range(a):
             val1.append(val1[i]+val1[i+1])
        print (val1[a-1], val1[a])
