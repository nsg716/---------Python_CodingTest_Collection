N = int(input())


for i in range(N):
    NN = int(input())
    for i in range(NN):
        a, b = map(int, input().split())
        print(a+b, a*b)