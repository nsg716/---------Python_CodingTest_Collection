i = int(input())
for i in range(i) :
    a ,b ,c = map (int, input().split())
    if (b-a > c):
        print("advertise") 
    elif (b-a < c) : 
        print("do not advertise")
    else: 
        print("does not matter")