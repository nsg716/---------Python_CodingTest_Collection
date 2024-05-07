import math
x = list(map(int, input().split()))
y = []
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            if x[i] == x[j] == x[k]:
                pass
            else:
                y.append(math.lcm(x[i],x[j],x[k]))
print(min(y))