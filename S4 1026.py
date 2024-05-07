N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
s = 0

for i in range(N):
    s += min(x)*max(y)
    x.pop(x.index(min(x)))
    y.pop(y.index(max(y)))
print(s)

# 재배열 부등식이라는 개념을 다루고 있다. 
N = int(input())
A =  sorted(map(int, input().split()))
B =  sorted(map(int, input().split()),reverse=True)
print(sum(A[i] * B[i] for i in range(N)))
# 12-05 중복 내용 추가