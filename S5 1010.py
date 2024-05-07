# 다리놓기 //순열 문제 순열 구현하기 

def factorial (a):
    b = 1
    for i in range(1, a+1) :
        b *= i
    return b
    

i = int(input())


for _ in range(i):
    a, b = map(int, input().split())
    result = factorial(b) // (factorial(a) * factorial(b - a))
    print(result)
"""
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)
    """