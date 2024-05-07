# 너비 우선 탐색 / 깊이 우선 탐색 
# 문제에서 경우의 수가 3^N으로 늘어 날 수 있으므로 , 동일한 경로는 탐색에서 제외하고, 최대 탐색이 26이라는 것을 알고 있어야 시간 초과가 나지 않는다.

from collections import deque
dy = (0,1,0,-1)
dx = (1,0,-1,0)

R,C = map(int,input().split())
board = [input() for _ in range(R)] # borad에 문자열을 담는다.
chk = [[set() for _ in range(C)] for _ in range(R)] # 체크할 리스트를 만든다. 시작점은 0 0  set 으로 한 이유는 같은 이동거리에 같은 문자는 무시한다는 의미
ans = 0

def is_vaild_cord (y, x): 
    return 0<= y < R and 0<= x < C

dq = deque()
chk[0][0].add(board[0][0]) # 문자열 삽입
dq.append((0,0,board[0][0])) # 문자열 삽입 + 이동거리를 잰다

while dq:
    y,x,s = dq.popleft() # 0 0 처음 알파벳
    ans = max(ans,len(s))

    for k in range(4): # 시작점을 기준으로 상하좌우 검색, 검색하여 1이 있는 경우 그 1이 2차원 배열에 없는 경우를 검색 
        ny = y + dy[k]
        nx = x + dx[k]
        if is_vaild_cord(ny,nx) and board[ny][nx] not in s: # 보드의 범위흫 벗어나지 않고 보드 안에 있으며, 새로운 문자 
            ns = s + board[ny][nx] # 문자를 더한다.
            if ns not in chk[ny][nx]: 
                chk[ny][nx].add(ns)
                dq.append((ny,nx,ns))
print(ans)
