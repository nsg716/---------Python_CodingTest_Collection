#최소 이동횟수 - 너비 우선탐색 
from collections import deque
import sys
input = sys.stdin.readline
dy = (-1,-2,-2,-1,1,2,2,1)
dx = (-2,-1,1,2,2,1,-1,-2)

l = 0

def isVaildCord (y, x): 
    return 0<= y < l and 0<= x < l 


for _ in range(int(input())):
    l = int(input())
    dq = deque()
    visited = [[False] * l for _ in range(l)]
    sy,sx = map(int,input().split()) # 시작 위치 
    gy,gx = map(int,input().split()) # 끝 위치 

    visited[sy][sx] = True
    dq.append((sy,sx,0))

    while dq :
        y,x,d = dq.popleft()

        if y == gy and x == gx:
            print(d)
            break

        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d+1
            if isVaildCord(ny,nx) and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((ny,nx,nd))
