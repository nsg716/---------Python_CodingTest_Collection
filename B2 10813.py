length, i = map(int,input().split()) # 바구니 길이 , 시행횟수 

x = [i for i in range(1, length+1)]# 이 문제의 핵심은 리스트가 생성할 때, 리스트 요소값이 주어지고 나서 시작이 되야 한다.
temp = 0

for i in range(i): # 공 위치 교한함수
    a, b = map(int, input().split())
    temp = x[a-1]
    x[a-1] = x [b-1]
    x [b-1] = temp

for i in range(length) :
    print (x[i], end = ' ')

