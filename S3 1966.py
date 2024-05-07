n = int(input())

for _ in range(n):
    N,M = map(int, input().split()) # 문서의 개수, 문서의 인덱스 설정으로 이해하면 졸을 듯 
    x = list(map(int,input().split())) # 문서의 중요도 
    
    result = 1
    while x:
        if x[0] < max(x):
            x.append(x.pop(0))
        else:
            if M == 0:
                break
            
            x.pop(0)
            result += 1
            
        M = M - 1 if M > 0 else len(x) - 1
    print(result)
            