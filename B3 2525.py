# 시간 계산 문제 합문제
H, M = map(int, input().split())
M1 = int(input())
if (M1+M) > 0 :
    new_H = H + int(((M1+M)/60))
    new_M = ((M1+M)%60)
    if new_H > 23 :
        new_H = new_H -24
else: 
    new_H = H
    new_M = M + M1
print(new_H, new_M)