# 출력 함수를 만들때 검토 많이 하자
length, i = map(int,input().split()) # 바구니 길이 , 시행횟수 
x = list(0 for i in range(0, length+1))
for i in (range(1, i+1)) :
    a, b, c = map(int, input().split())
    for j in range(a-1, b) :
        x[j] = int(c) # 여기가 중요한 포인트라고 생각

for i in (range(0, length)) : # 실제로 여기서 범위를 잘못 생각해서 꼬임 
    print(x[i], end = ' ')
    
    