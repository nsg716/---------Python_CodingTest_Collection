N = int(input())

max = 0
for i in range(N):
    M = int(input())
    for j in range(M):
        a, b = input().split()
        b = int(b)
        if (b > 0):
            if (b > max):
                max = b
                L = a
    print(L)