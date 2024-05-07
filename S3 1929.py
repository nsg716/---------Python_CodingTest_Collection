# 이 부분은 소수 구하기 문제이기 때문에 다시 공부하기

a,b = map(int, input().split())
s = []

for i in range(a-1,b):
    s.append(i+1)

for i in range(a,b+1):
    if i== 1 :
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else :
        print(i)
