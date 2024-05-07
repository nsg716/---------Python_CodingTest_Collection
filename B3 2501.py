N, M = map(int, input().split()) 
x = []
for i in range(1,N+1):
    if N%i == 0 : 
        x.append(i)

if M > len(x):
    print("0")
else :    
    print(x[M-1])