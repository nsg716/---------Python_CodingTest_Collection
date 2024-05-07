# 문제 4번  - 시뮬레이션 구현 문제,  문제에서 명시한 것들을 정확하게 구현을 하였는지 검증하는 경향이 크다. 
# 어려운 자료구조나 알고리즘은 사용하지 않았으므로, 어떤 식으로 구현할 지 구체적인 방면에 초점을 두어야 한다.

dy = (0, 0, 0, -1, 1)
dx = (0, 1, -1, 0, 0)

N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 7

def is_vaild_coord(y,x):
    return 0 <= y < N and 0 <= x < M

for d in list(map(int,input().split())):
    ny = y + dy[d]
    nx = x + dx[d]
    if not is_vaild_coord(ny,nx):
        continue

    next_dice = dice[:]
    if d == 1: # 동쪽 
        next_dice[1] = dice[4]
        next_dice[3] = dice[1]
        next_dice[6] = dice[3]
        next_dice[4] = dice[6]
    elif d== 2 : # 서쪽
        next_dice[1] = dice[3]
        next_dice[3] = dice[6]
        next_dice[6] = dice[4]
        next_dice[4] = dice[1]
    elif d== 3 :  # 북쪽
        next_dice[1] = dice[5]
        next_dice[2] = dice[1]
        next_dice[6] = dice[2]
        next_dice[5] = dice[6]
    else : # 남쪽
        next_dice[1] = dice[2]
        next_dice[2] = dice[6]
        next_dice[6] = dice[5]
        next_dice[5] = dice[1]
        
    dice = next_dice[:]
    if board[ny][nx] == 0:
        board[ny][nx] = dice[6]
    else:
        dice[6] = board[ny][nx]
        board[ny][nx] = 0 

    y = ny
    x = nx
    print(dice[1])