a = list(input())
a.sort()
a.reverse()
for i in range(len(a)):
    print(*a[i], end = "")