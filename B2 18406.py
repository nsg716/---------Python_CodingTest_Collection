# 럭키 스트레이트
# 구현

N = list(input())
length_N = len(N)//2
x1 = sum(int(i) for i in N[:length_N])
x2 = sum(int(i) for i in N[length_N:])

if x1 == x2:
    print("LUCKY")
else:
    print("READY")

