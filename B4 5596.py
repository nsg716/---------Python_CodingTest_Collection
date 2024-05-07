sum1 = [0,0]

for i in range(2):
    a, b, c, d = map(int, input().split())
    sum1[i] += a
    sum1[i] += b
    sum1[i] += c
    sum1[i] += d

if sum1[0] >= sum1[1]:
    print(sum1[0])
else:
    print(sum1[1])