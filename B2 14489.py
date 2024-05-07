N , M = map(int,input().split())
ans = int(input())
if N+M >=2*ans :
    print((N+M) -(2*ans))
else:
    print(N+M)