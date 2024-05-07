x = [False] * 1001
N, L = map(int,input().split()) # 구멍 개수, 테이프 길이 입력
for i in map(int, input().split()): # 구멍마다 얼마나 간격이 있는지 입력
    x[i] = True
ans, a = 0,0
while a<= 1000:
    if x[a]: # 구멍이 있는 부분의 조건문 실행 
        ans+=1 # 막은 횟수
        a +=L # 구멍으로 부터 얼마나 테이프를 썼는지 
    else:
        a+=1 # 구멍이 막혔으면 다음으로 넘어감 
print(ans)
# 시간 복잡도는 O(1000)이지만 횟수 많아 질 수 있으므로 O(n)이다.

