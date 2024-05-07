a, b= map(int, input().split())
x= []
for i in range(1,50):
    for j in range(i):
       x.append(i)

print(sum(x[a-1:b])) 