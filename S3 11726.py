# 동적 계획법은 다른 말로 다이나믹 프로그래밍이라고도 한다. 

# 점화식은 f(n) {if n == 1 , 1} {if n == 2 ,2 } {if n >= 3 , f(n-1)+f(n-2)}

import sys

sys.setrecursionlimit(10**6)

n = int(input())
cache = [0] * (n+1)

def f(n):
    if cache[n]:
        return cache[n]
    
    cache[n] = n if n <= 2 else (f(n-1)+ f(n-2))%10007

    return cache[n]

print(f(n))