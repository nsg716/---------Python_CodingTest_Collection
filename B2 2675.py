# 문자열 인덱싱 응용 
i = int(input())
i1 = 0
for i in range(1, i+1):
    a, b = map(str,input().split())
    new_b = list(b)
    new_a = int(a)
    for il in range(len(new_b)):
        print(new_b[il]*new_a, end="")
    print()