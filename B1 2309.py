x = []
for i in range(9):
    x.append(int(input()))

x.sort()
Sum = sum(x)
for a in  range(9):
    for b in  range(a+1, 9):
        if (Sum - x[a] - x[b] == 100):
            aa = x[a]
            bb = x[b]


x.remove(aa)
x.remove(bb)
x.sort()
for i in range(7):
    print(x[i])                      
                  