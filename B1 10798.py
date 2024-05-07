x = []
for i in range(5):
    line= input()
    x.append(line)

max_length = max(len(line) for line in x)

for j in range(max_length):
    for i in range(5):
        if j<len(x[i]):
            print(x[i][j],end="")
        
