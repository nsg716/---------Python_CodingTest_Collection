# 중요한 점은 2차원 배열이라는 것 
# 가로 또는 세로 하나를 바꿨을 때, 같은 문자면 ans에 저장하는 것 
# 가로 검사하는 방법과 세로 검사하는 방법 두가지를 함수로 구현 
# 위치를 바꾸고 다시 정립하는 것
# 시간복잡도는 O(N^4) 이다.

N = int(input())
board = [list(input()) for _ in range(N)]
ans = 1

def search ():
    global ans # 전역 변수 선언 
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if board[i][j-1] == board[i][j]:
                cnt += 1
                ans = max(ans,cnt)
            else :
                cnt = 1
    for j in range(N):
        cnt = 1
        for i in range(1,N):
            if board[i-1][j] == board[i][j]:
                cnt += 1
                ans = max(ans,cnt)
            else :
                cnt = 1

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            search()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 원상복구
        if i+ 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            search()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 원상복구
print(ans)