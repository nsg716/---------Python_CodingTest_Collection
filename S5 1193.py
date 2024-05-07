import sys
N = int(sys.stdin.readline())

sum=1
while N>sum:
    N -= sum
    sum +=1

if sum % 2 ==0:
    a = N
    b = sum-N+1

else : 
    a = sum-N+1
    b = N
    
print(a ,'/',b , sep='')