
a = int(input())
b = int(input())
s = []
x = []
for i in range(a-1,b):
    s.append(i+1)

for i in range(a,b+1):
    if i== 1 :
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else :
        x.append(i)
if len(x) == 0:
    print("-1")
else :
    print(sum(x))
    print(min(x))
