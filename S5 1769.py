N = list(input())
sum1 = 0 
count= 0
while len(N) > 1:
    count += 1
    for i in range(len(N)):
        sum1 += int(N[i])
    N = []
    N = list(str(sum1)) 
    sum1 = 0
print(count)
if int(N[0]) % 3 == 0:
    print("YES")
else :
    print("NO")