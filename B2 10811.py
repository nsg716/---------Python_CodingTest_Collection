length, i = map(int,input().split()) # 바구니 길이 , 시행횟수 

x = [i for i in range(1, length+1)] # 리스트에 요소 추가
temp = 0

for i in range(i): # 바구니 순서 위치 교한함수
    a, b = map(int, input().split())
    temp = x[a-1:b]
    temp.reverse()
    x[a-1:b] = temp

for i in range(length) :
    print (x[i], end = ' ')

