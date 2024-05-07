N = int(input())
res = N
count = 0
while res != 1:
    count += 1
    if (res % 2 == 0):
        res /= 2
    else:
        res += 1
print(count)