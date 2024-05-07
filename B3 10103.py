i = int(input())
sum1 = 100
sum2 = 100
for i in range(i):
    a, b = map(int, input().split())
    if a > b :
        sum2 -= a
    elif a < b :
        sum1 -= b
    
print(sum1)
print(sum2)