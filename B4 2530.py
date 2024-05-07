# 시간 계산 초 문제 합문제( 나중에 다시하기)
H, M, S = map(int, input().split())
S1 = int(input())
#  초계산
sec  = ((S1+S)%60)
M1 = ((S1+S)//60)
# 분계산
min = ((M+M1)%60)
H1 = ((M+M1)//60)
# 시계산
hour = (H1 + H)%24


print (hour,min,sec)