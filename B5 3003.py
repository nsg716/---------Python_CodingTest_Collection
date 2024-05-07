# 요소가 있는 리스트 선언 이후, 입력된 값과 비교를 하면서 조건에 따른 출력 
x = [1,1,2,2,2,8] # 기존의 리스트 
y = list(i for i in range(0,6)) # 입력받을 리스트
z = list(i for i in range(0,6)) # 출력할 리스트

a, b, c, d, e, f = map(int, input().split())
y[0] = a
y[1] = b
y[2] = c
y[3] = d
y[4] = e
y[5] = f
for i in range(0, 6):
    if y[i] > x[i] :
        z[i] = x[i] - y[i]
    elif y[i] < x[i] :
        z[i] = x[i]-y[i]
    elif y[i] == x[i]:
        z[i] = 0
for i in range(0,6):
    print(z[i], end= ' ')