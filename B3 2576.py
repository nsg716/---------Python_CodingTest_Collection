x = []
y = []
error = 0
for i in range(7):
    x.append((int(input())))
for i in range(len(x)):
    if (x[i] % 2 != 1):
        error +=1
    
    elif (x[i] % 2 == 1):
        y.append(x[i])
if (error == 7):
    print("-1")
else :
    print (sum(y))
    print(min(y))
            
