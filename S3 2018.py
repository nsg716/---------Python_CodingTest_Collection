import sys 

input = sys.stdin.readline

x = []

N = int(input())

for i in range(N):
    x.append(int(input()))

x.sort()


x_ave = round(sum(x)/len(x))
print(x_ave)
    
print(x[(len(x)//2)])

dic = dict()
for i in x:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
a = max(dic.values())
list_max = []

for i in dic:
    if a == dic[i]:
        list_max.append(i)

if len(list_max) > 1:
    print(list_max[1])
else:
    print(list_max[0])
    
print(max(x) - min(x))


    
    

