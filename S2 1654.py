import sys
imput = sys.stdin.readline
K,N = map(int,input().split())
x = [int(input()) for _ in range(K)]
start,end = 1,max(x)

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for i in x:
        count += i // mid
        
    if count >= N:
        start = mid + 1     #분모가 증가함으로 써 더 적은 N개가 나온다.
    else :
        end = mid - 1       #분모가 감소함으로 써 더 많은 N개가 나온다.
    # print(count, end = " ") # count의 개수 확인용 
    # 결국에는 start  == end 가 되서 반복문이 멈춘다.

# 멈췄을 때 그 길이 

print(end)