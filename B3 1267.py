N = int(input())
a,b = 0,0
count1,count2 = 0,0
x = list(map(int,input().split()))
for i in range(N):
    
    a = x[i] // 30
    b = x[i] // 60
    count1 += 10*a+10
    count2 += 15*b+15

if count1 < count2 :
    print("Y", end = " ")
    print(count1)
elif count1 > count2 :
    print("M" , end = " ")
    print(count2)
elif count1 == count2: 
    print("Y M" , end = " ")
    print(count1)
