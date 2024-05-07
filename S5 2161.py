N = int(input())
x = list(i+1 for i in range(N))
y = []
while len(x) != 1 :
        y.append(x.pop(0))
        x.append(x.pop(0))
for i in y:
    print (i , end = ' ')

print(x[0])