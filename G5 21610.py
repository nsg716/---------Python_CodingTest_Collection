# 문제 7번 
# 시뮬레이션 문제,3차원 문제이므로 2차원 배열을 2개 합쳤다. 플래그 변수 C를 사용 C를 변경하기위한방법은 총 3가지 있다. 
# 1-c , (c+1) % 2, c^1로 총 3가지로 셋 중 하나를 사용하면 된다.
 

dy = (-1, -1, 1, 1)
dx = (-1, 1, -1, 1)
ddy = (0, -1, -1, -1, 0, 1, 1, 1)
ddx = (-1, -1, 0, 1, 1, 1, 0, -1)

N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
clouds = [[[False] * N for _ in range(N)] for _ in range(2)]
c = 0
for i in range(N-2,N):
    for j in range(2):
        clouds[c][i][j] = True

def is_vaild_coord(y,x):
    return 0 <= y < N and 0 <= x < N

for _ in range(M):
    d,s = map(int, input().split())
    for y in range(N):
        for x in range(N):
            if clouds[c][y][x]:
                ny = (y + ddy[d-1] * s + N * 50) % N
                nx = (x + ddx[d-1] * s + N * 50) % N
                clouds[c^1][ny][nx] = True
                A[ny][nx] += 1

    for y in range(N):
        for x in range(N):
            if clouds[c^1][y][x]:
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if is_vaild_coord(ny,nx) and A[ny][nx]:
                        A[y][x] += 1

    for y in range(N):
        for x in range(N):
            if not clouds[c^1][y][x] and A[y][x] >= 2:
                A[y][x] -=2
                clouds[c][y][x] = True
            else:
                clouds[c][y][x] = False

    for y in range(N):
        for x in range(N):
            clouds[c^1][y][x] = False

print(sum(sum(i) for i in A))