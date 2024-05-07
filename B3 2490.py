x =[]
for i in range(3):

    x.append(list(map(int, input().split())))
 
for i in range(3):
    if (sum(x[i]) == 0):
        print("D")
    elif (sum(x[i]) == 1):
        print("C")
    elif (sum(x[i]) == 2):
        print("B")
    elif (sum(x[i]) == 3):
        print("A")
    elif (sum(x[i]) == 4):
        print("E")
