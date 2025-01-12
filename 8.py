N = int(input())
x = []
result = 1
x = list(input().split()) 
x.sort()
for i in range(len(x)):
    if i != int(x.pop(0)):
       result = -1

print(result)
