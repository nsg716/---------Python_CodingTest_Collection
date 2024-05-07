# 기출문제 2번 
# 보드를 한 방향으로 미는 것을 반복 + 보드를 90도 회전하는 것으로 해결 
# 보드의 회전방향과 어느 방향으로 미는지는 답에는 영향이 없다.

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def rotate_board(b):
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[i][j] = b[j][N - 1 -i]

    return ret

def push_left(b):
    ret = [[0] * N for _ in range(N)]
    for i, r in enumerate(b):
        row = r[:]
        while 0 in row:
            row.remove(0)

        nrow = []
        j = 0
        while j < len(row):
            if j+1 < len(row) and row[j] == row[j+1]:
                nrow.append(row[j] << 1)
                j += 2
            else:
                nrow.append(row[j])
                j += 1

            
        for j in range(len(nrow)):
            ret[i][j] = nrow[j]

    return ret

def dfs(b,d):
    global ans
    for i in range(N):
        for j in range(N):
            ans = max(ans,b[i][j])

    if d < 5:
        nd = d + 1
        dfs(push_left(b), nd)
        for k in range(3):
            b = rotate_board(b)
            dfs(push_left(b),nd)

dfs(board, 0)
print(ans)
