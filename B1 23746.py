# 문자열 압축 해제
# 구현

 
N = int(input())
res = []
for _ in range(N):
    x = list(map(str, input().split()))

    res.append(x)

y = list(input())
result=""
for i in y:
    for j in range(N):
        if (res[j][1] == i):
            result += "".join(res[j][0])
    
m1,m2 = map(int, input().split())
print(result[m1-1:m2])

