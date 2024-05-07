# 피보나치 함수 주어진 갑을 계산할 수 있다.

fib = [0,1]
N = int(input())
for i in range(N):
    fib.append(fib[i]+fib[i+1])
print(fib[N])