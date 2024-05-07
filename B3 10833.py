N = int(input())
sum1 = 0
for i in range(N):
    a, b = map(int, input().split())
    sum1 += (b%a)

print(sum1)