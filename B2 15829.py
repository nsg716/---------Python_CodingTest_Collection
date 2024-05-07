N = int(input())

x = list(input())
sum = 0
for i in range(N):
    sum += ((ord(x[i])-96)*31**i)
print(sum % 1234567891) # 문제 내용에서 해시값 충동을 막기 위한 서로소 값이 주어짐 이를 충돌 방지용으로 구현