# 시각
# 브루트포스 알고리즘

N,K = map(int, input().split())
K = str(K)
cnt = 0
for i in range(N+1):
    if i < 10:
        i = "0" + str(i)
    for j in range(60):
        if j < 10:
            j = "0" + str(j)
        for k in range(60):
            if k < 10:
                k = "0" + str(k)
            if K in (str(i) + str(j) + str(k)):
                cnt += 1
                
print(cnt)