# 전형적인 길찾기 문제이고, 최단시간을 구하는 문제이기에 너비우선탐색 (BFS)를 사용한다.
from collections import deque
dy = (0,1,0,-1)
dx = (1,0,-1,0)

N, M = map(int, input().split())
borad = [input() for _ in range(N)]
chk = [[False] * M for _ in range(N)]
dq = deque()
dq.append((0,0,1))
chk [0][0] = True # 시작점은 항상 같다.

def is_vaild_cord (y, x):
    return 0<= y < N and 0<= x < M

while len(dq) > 0:
    y, x, d = dq.popleft() # 0 0 1 을 차례대로 초기화 # 큐의 시작 값 

    if y == N - 1 and x == M -1:
        print(d)
        break # 끝에 도착 이동한 거리 만큼 출력 d의 의미는 거리 

    for k in range(4): # 시작점을 기준으로 상하좌우 검색, 검색하여 1이 있는 경우 그 1이 2차원 배열에 없는 경우를 검색 
        ny = y + dy[k]
        nx = x + dx[k]
        nd = d + 1 
        if is_vaild_cord(ny,nx) and borad[ny][nx] == '1' and not chk[ny][nx]:  # 범위안의 있는 1이 맞는지 확인 하는 절차 
            chk[ny][nx] = True #1이 있는 부분을 변경 
            dq.append((ny,nx,nd)) # 큐에 저장 
