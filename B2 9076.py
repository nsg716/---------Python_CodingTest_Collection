
N = int(input())
for i in range(N):
    x = list(map(int, input().split()))
    x.pop(x.index(max(x)))
    x.pop(x.index(min(x)))
    if max(x) - min(x) >= 4:
        print("KIN")
    else : 
        print(sum(x))
