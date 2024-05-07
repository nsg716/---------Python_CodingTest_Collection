a, b = map(int, input().split())

if (a > b):
    temp = b
    b = a
    a = temp
if (a == b):
    print(a-b)
else : 
    print(b-a-1)
for i in range(a+1, b):
    print(i, end = ' ')