# 시간 계산 문제 고정 감소
H, M = map(int, input().split())
ch = M - 45
if ch < 0 :
    new_H = H -1
    new_M = 60 + ch
else: 
    new_H = H
    new_M = ch
if new_H < 0:
    new_H = 23
print(new_H, new_M)