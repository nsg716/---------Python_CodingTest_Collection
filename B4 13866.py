import math
x = list(input().split())
x= list(map(int, x))
max= 0
min = 1000000
for i in range(len(x)): 
    if (int(x[i]) > int(max)):
        max = x[i]
        
    if (int(x[i]) < int(min)):    
        min = x[i]
print (abs((sum(x)-min-max) - (min+max)))