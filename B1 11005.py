a, b = map(int, input().split())


def exchange (n, base):
    L = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q,r = divmod(n, base) # q에 몫, r에 나머지 

    return exchange(q,base) + L[r] if q else L[r] # q를 계속 나누어서 나머지를 연결 재귀함수 성짛 
print(exchange(a,b))