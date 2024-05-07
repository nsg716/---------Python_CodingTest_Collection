x = list(0 for i in range(0,9))
for i in (range(9)) : 
    x[i] = int(input())

print (max(x))
print (x.index(max(x))+1)