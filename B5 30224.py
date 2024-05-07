a = str(input())

if (a.count('7') == 0 and int(a) % 7 !=0 ):
    print(0)
elif(a.count('7') == 0 and int(a) % 7 ==0):
    print(1)
elif(a.count('7') >= 1 and int(a) % 7 !=0):
    print(2)
elif(a.count('7') >= 1 and int(a) % 7 ==0):
    print(3)