N = int(input())
n = N
count = 0

while True:
    a = n // 10
    b = n %10
    c = (a+b)%10
    n = (b*10) +c
    count += 1
    if (n==N):
        break
print(count)

