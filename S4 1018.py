# 완전탐색 # O(n^2)
"""
N,M = map(int,input().split())
board = [input() for _ in  range(N)]
ans = N*M

def fill(y,x,bw):
    global ans 
    cnt = 0
    for i in range(8): # 8 X 8 체스판 제작 
        for j in range(8):
            if (i+j) % 2:
                if board[y+i][x+j] == bw:
                    cnt += 1
            else :
                if board[y+i][x+j] != bw:
                    cnt +=1
    ans = min(ans,cnt)

for y in range(N-7):
    for x in range(M-7):
        fill(y,x,'B')
        fill(y,x,'W')
print(ans)
"""
# 다이나믹 프로그래밍 // 누적합이라는 개념 사용 누적합 대신 연속합 혹은 구간합이라고도 한다. 
# 반복문으로 다시 구하는 것보다 누적합으로 구하는 것이 더 효율적인다. 
# 첫글자가 B 인경우는 O(1), 첫글자가 W 인경우는  O(n^2) 걸린다.
N,M = map(int,input().split())
board = [input() for _ in range(N)]
ans  = N*M 

def make_acc(bw):
    global ans 
    acc = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i > 0:
                acc[i][j] += acc[i-1][j]
            if j > 0:
                acc[i][j] += acc[i][j-1]
            if i > 0 and j > 0:
                acc[i][j] -= acc[i-1][j-1]
            if (i+j) % 2 and board[i][j] == bw:
                acc[i][j] += 1
            if (i+j) % 2==0 and board[i][j] != bw:
                acc[i][j] += 1
    for i in range(N-7):
        for j in range(M-7):
            cnt = acc[i+7][j + 7]
            if i > 0:
                cnt -= acc[i-1][j+7]
            
            if j > 0:
                cnt -= acc[i+7][j-1]

            if i > 0 and j > 0 :
                cnt += acc[i-1][j-1]
            
            ans = min(ans,cnt)


make_acc('B')
make_acc('W')
print(ans)
            