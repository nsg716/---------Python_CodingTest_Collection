N = int(input())
print("Gnomes:")
for i in range(N):
    a, b, c =map(int, input().split())
    if a > b:
        if b > c :
            print("Ordered")
        else :
            print("Unordered")
    if a < b : 
        if b < c :
            print("Ordered")
        else :
            print("Unordered")