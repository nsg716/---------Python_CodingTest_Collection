# 배열 을 정렬 
N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
chk= [False] * N
p = []
for i in A:
    for j in range(B.index(i),N):
        if i == B[j] and not chk[j]:
            chk[j] = True
            p.append(j)
            break

print(" ".join(map(str,p)))
