N = int(input())
for j in range(N):
    x = list(map(str, input().split()))
    x[0] = float(x[0])
    for i in range(len(x)):
        if x[i] == "@":
            x[0] *= 3
        elif x[i] == "%":
            x[0] += 5
        elif x[i] == "#":
             x[0] -= 7
    print("{:.2f}". format(x[0]))