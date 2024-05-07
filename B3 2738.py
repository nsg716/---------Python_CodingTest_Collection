a, b = map(int, input().split())

x1, x2 = [],[]

for i in range(a):
   row = list(map(int, input().split()))
   x1.append(row)

for i in range(a):
   row = list(map(int, input().split()))
   x2.append(row)

for i in range(a):
    for j in range(b):
        print(x1[i][j] + x2[i][j], end = ' ')
    print()
 

