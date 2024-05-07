# 계산하기
x = list(0 for i in range(30))

for i in range(30) : 
    x[i]=i+1

for i in range(28) : 
    data = int(input())
    x.remove(data)

for i in range(2) : 
    print(x[i])
