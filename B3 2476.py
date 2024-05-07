i = int(input())

sum = [i for i in range(i)]
for i in range(i) :
    a,b,c = map(int, input().split())

    if (a == b == c) :
        sum[i] = (10000+a*1000)
    elif(a == b):
        sum[i] = (1000+ a * 100)
    elif(a == c): 
        sum[i] = (1000+ a * 100)
    elif (b == c) : 
        sum[i] = (1000+ b * 100)
    elif (a > b) :
        if a > c : 
            sum[i] = (a * 100)
        else : 
            sum[i] = (c * 100)
    elif a < b:
        if b >  c:
            sum[i] = (b*100)
        else :
            sum[i] = (c*100)
    elif (a < c):
        if b > c :
            sum[i] = (b * 100)
        else :
            sum[i] = (c*100)

print(max(sum))

