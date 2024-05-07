N = int(input())
a = list(map(int,input().split()))
count = 0

for i in range(len(a)):
    error = 0
    if a[i] > 1:
        for j in range(2,a[i]):
            if a[i] % j == 0:
                error += 1
        if error == 0:
            count += 1            
print(count)