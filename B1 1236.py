# 이차원 배열 문제해결에 가까움

a, b = map(int, input().split())
count1 = 0
count2 = 0
x= []
for i in range(a):
    x.append(input())
    

for i in range(a): # 가로 횟수
    if 'X' not in x[i]:
        count1 +=1
for j in range(b): # 세로 횟수
    if 'X' not in [x[i][j] for i in range(a)]:
        count2 += 1

print(max(count1,count2))

