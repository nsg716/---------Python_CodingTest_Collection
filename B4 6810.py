# 이문제는 짝수번 (0번 포함) * 1, 홀수 번 *3을 하는 것
# 9780921418 + 마지막 3자리가 주어지고, 이들의 합을 구하는 것이 문제
# 9780921418는 91

a = int(input())
b = int(input())
c = int(input())
result = 91+ a*1 + b* 3+ c* 1
print("The 1-3-sum is %d" %result)