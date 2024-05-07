# doit 파이썬 코테 준비 : 045번
# 확장 유클리드 호재법 : 오른쪽 변의 값이 gcd (A,B)를 만족하면 재귀를 이용해서 aX + bY = A 형태의 값을 구할 수 있다.

a, b, c = map(int, input().split())
 

def gcd (a,b):
    if b == 0 :
        return a
    else :
        return gcd(b,a%b)
    
def Execute(a,b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret 
    q = a// b
    v = Execute(b,a%b)
    ret[0] = v[1]
    ret[1] = v[0] - v[1] *q
    return ret
    
mgcd = gcd(a,b)

if c % mgcd !=0 :
    print(-1)
    
else:
    mok = int(c/ mgcd)
    ret = Execute(a,b)
    print(ret[0] * mok, end = ' ')
    print(ret[1] * mok)