import math
N = int(input())

for i in range(N):
    sum = 0
    x = list(input().split())
    for i in range(1,len(x)):
        for j in range(i+1,len(x)):
            sum+=  math.gcd(int(x[i]),int(x[j]))
            
                
    print(sum) 
