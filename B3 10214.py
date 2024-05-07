i = int(input())
sum1 = 0
sum2 = 0
for i in range(i) :
    for i in range(9) : 
        a, b = map(int, input().split())
        sum1 += a
        sum2 += b
    if sum1 > sum2 :
        print ("Yonsei")
    elif sum1 < sum2 : 
        print ("Korea")
    else :
        print("draw")