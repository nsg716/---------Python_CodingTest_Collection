# A+B - 8
i = int(input())
x = list(0 for i in range(0,i))
y = list(0 for i in range(0,i)) # a 저장 
z = list(0 for i in range(0,i)) # b 저장
for i in range(1,i+1):
    a, b = map(int, input().split())
    y[i-1] = a
    z[i-1] = b
    x[i-1] = a + b 
    
for i in range(1, i+1):
    print("Case #%d: %d + %d = %d" %(i,y[i-1],z[i-1],x[i-1]) )