N = int(input())
x = []
for i in range(N):
    x.append(input())


for i in range(N-1):
    for j in range(i,N):
        if x[i][::-1] == x[j]:
            print(len(x[i]), x[i][len(x[i])//2])
            break