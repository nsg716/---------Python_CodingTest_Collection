a1 = int(input())
a2 = int(input())
a3 = int(input())

b1 = int(input())
b2 = int(input())
b3 = int(input())
sum1 = a1*3+a2*2+a3
sum2 = b1*3+b2*2+b3

if sum1 > sum2: 
    print("A")
elif(sum1 < sum2):
    print("B")
else :
    print("T")