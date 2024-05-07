N = int(input())

for i in range(N):
    lang= "*" * int(2*(N-i)-1)
    print(' '* i + lang)