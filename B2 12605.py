N = int(input())
for i in range(N):
    x =list(input().split())
    x.reverse()
    print("Case #%d:" %(i+1), end = ' ')
    for i in range(len(x)):
        print(x[i], end = ' ')
    print()