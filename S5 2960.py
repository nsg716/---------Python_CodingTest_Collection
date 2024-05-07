N, K = map(int, input().split())
N1 = [i for i in range(2, N+1)]
x1 = []
c = 0
minN1 = N1[0]
while c < K:
    i = 1
    
    while minN1 * i < N + 1:
        
        if minN1 * i in N1:
            c += 1
            N1.remove(minN1 * i)
            
            if c == K:
                res = minN1 * i # 욋수에 지워진 부분
        i += 1

    if len(N1) > 0:
        minN1 = N1[0]
print(res)