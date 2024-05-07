N = int(input())

for i in range(N):
    star = "*" * int(i*2+1)
    print(" " * (N-i-1) + star)