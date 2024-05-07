N = int(input())

for a in range(N):
    x = list(input())
    count = 0
    error = 0
    for i in range(len(x)):
        if (x[i] == "("):
            count += 1
        elif( x[i] == ")"):
            count -= 1
        if (count < 0):
            error += 1
    if count == 0 and error == 0:
        print("YES")
    else : 
        print("NO")