sum = 0
for i in range(5):
    i = int(input())
    if (i < 40) : 
        i = 40
    sum += i
print(int(sum/5))