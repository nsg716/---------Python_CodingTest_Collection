# 분해합

N = int(input())

for i in range(1,N+1):
    num = sum((map(int,str(i))))
    num_sum = i + num # 분해합 = 생성자 + 각 자릿수의 합
    
    if num_sum == N:
        print(i)
        break
    if i == N:
        print(0)