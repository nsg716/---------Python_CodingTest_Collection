N = int(input())

sum2 = 0
for i in range(1,N):
    sum2 += i*N+i
print(sum2)


"""
x = 0
sum1 = 0
while 1:
    x += 1
    if x % N == x // N:
        sum1 += x
    if x // N > N:
        break
print(sum1)
"""