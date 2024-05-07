# doit 파이썬 코테 준비 : 043번
# 유클리드 호재법 : 최대 공약수를 구하는 문제 

def gcd (a,b):
    if b == 0 :
        return a
    else :
        return gcd(b,a%b)
    
a, b = map(int, input().split())
result = gcd(a,b)

while result > 0:
    print(1,end = '')
    result -= 1 