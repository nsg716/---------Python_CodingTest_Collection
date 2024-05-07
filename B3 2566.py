x= []
y = []

for i in range(9):
    a = (list(map(int, input().split())))
    x.append(a)

for i in range(9):
    y.append(max(x[i]))
    

print(max(y))
row = int(y.index(max(y)))+1
pow = int(x[row-1].index(max(x[row-1])))+1
print(row, pow)
