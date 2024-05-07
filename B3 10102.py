i = int(input())
a = list(input())
sum1 = 0
sum2 = 0
for i in range(i):
    if (a[i] == "A"):
        sum1 += 1
    else :
        sum2 += 1
if  sum1 > sum2:
    print("A")
elif (sum2 > sum1):
    print("B")
else :
    print("Tie")
