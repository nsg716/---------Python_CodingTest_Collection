i =  int(input())
pow1 = 1
if (i == 0):
    print(pow1)
else:
    for i in (range(1,i+1)):
        pow1 *= i
    print(pow1)