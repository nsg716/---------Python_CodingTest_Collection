N = int(input())
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 %a2== 0:
    res1 = a1/a2
else:
    res1 = int(a1/a2)+1
if b1 %b2== 0:
    res2 = b1/b2
else:
    res2 = int(b1/b2)+1
    
x = []
x.append(res1)
x.append(res2)
print(int(N-max(x)))
