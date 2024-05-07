x1 = []
for i in range(3):
    x1.append(input())

sum = 0
sum1 = 1
count = 10
color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
for i in range(2):
    for j in range(len(color)):
        if x1[i] == color[j]:
            
            sum += count*color.index(color[j])
            count -= 9

for j in range(len(color)):
    if x1[-1] == color[j]:
        sum1 *= 10**color.index(color[j])
print(sum*sum1)