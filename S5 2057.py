N = int(input())
if N == 0:
    print("NO")
else : 
    mul = 1
    x = [1]
    for i in range(20):
        mul *= i+1 # 1!부터 시작
        x.append(mul)

    for i in range(20,-1,-1):
        if N >= x[i]:
            N-= x[i]
            
    if N == 0:
        print("YES")
    else :
        print("NO")


