# 거스름돈이 싫어요
# 수학, 유클리드 호재법
import math

N = int(input())

items = [list(map(int, input().split())) for _ in range(N)]
dividend = [i[0] for i in items]


# 분모 맞추기 
divisor  = 1
for _ , divider  in items:
    divisor *= divider

# 분자 맞추기 
for i in range(len(dividend)):
    dividend[i] *= divisor // items[i][1]
  
GCD = dividend[0]
for i in range(1,len(dividend)):
     GCD = math.gcd(GCD, dividend[i])


GCD_result = math.gcd(GCD,divisor)
print(f'{GCD//GCD_result} {divisor//GCD_result}')



