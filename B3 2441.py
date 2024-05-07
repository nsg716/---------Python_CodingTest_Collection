N = int(input())

for i in range(N):
    star = "*" * int(N-i)
    print(star.rjust(N))