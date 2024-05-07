x = []
for i in range(3):
    x.append(int(input()))

for i in range(len(x)):
    if x[i] > min(x):
        if x[i] < max(x):
            print(x[i])