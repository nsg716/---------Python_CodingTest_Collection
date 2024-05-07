price = int(input())
i = int (input())
sum = 0
x = list(0 for i in range(0,i))
for i in range(1,i+1):
    a, b = map(int,input().split())
    x [i-1]= a*b

for i in range(1, i+1):
    sum += int(x[i-1])

if (sum == price):
    print("Yes")
else:
    print("No")