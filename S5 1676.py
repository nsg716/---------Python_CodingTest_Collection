N = int(input())
sum = 1
count = 0
for i in range(1,N+1):
    sum *= i

x = list(str(sum))
x.reverse()


for i in range(len(x)):
    if x[i] == '0':
        count += 1
    else:
        break
print(count)