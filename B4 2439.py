a = int(input())
x = list(0 for a in range(0,a))
i = 1
for i in range(1,a+1): 
    x[a-1] = "*" * i
    print(x[a-1].rjust(a))

    