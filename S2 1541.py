# doit 파이썬 코테 준비 : 036번
# 연산자 사이의 최대란 작은수 만들기
answer = 0
A= list(map(str, input().split("-")))

def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        answer += temp
    else: 
        answer -= temp
print(answer) 