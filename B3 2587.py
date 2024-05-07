x = []
y= []
for i in range(5):
    x.append(int(input()))


print(int(sum(x)/len(x)))
y = sorted(x)

print(y[int(len(x)/2)] )