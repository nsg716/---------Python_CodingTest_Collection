import sys
sys.setrecursionlimit(10**6)#  탐색 횟수 설정 

dy = (0,1,0,-1)
dx = (1,0,-1,0)

N,M,K = map(int, input().split())
borad = [[','] * M for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    borad[y-1][x-1] = '#' # 보드에 음식물이 있는 위치

visited = [[False] * M for _ in range(N)]
sz = 0
ans = 0

def isVaildCord (y, x): 
    return 0<= y < N and 0<= x < M

def dfs (y,x): # 있으면 사이즈 증가 + 그근처에 # 이 있는지 확인 , 있으면 사이즈를 갱신
    global ans, sz # 전역변수 선언 

    visited[y][x] = True # 음식물이 있는 위치 
    sz+=1
    ans = max(ans,sz) # 여러개의 음식물중 가장 큰 음식물초기화 

    for k in range(4): # 시작점을 기준으로 상하좌우 검색, 검색하여 1이 있는 경우 그 1이 2차원 배열에 없는 경우를 검색 
        ny = y + dy[k]
        nx = x + dx[k]
        if isVaildCord(ny,nx) and not visited[ny][nx] and borad[ny][nx] == '#': # 보드의 범위흫 벗어나지 않고 보드 안에 있으며, #이 있는지 확인 
            dfs(ny,nx)

for i in range(N):
    for j in range(M):
        if not visited[i][j] and borad[i][j] == '#': # 배열에 방문하지 노드 탐색 
            sz = 0
            dfs(i,j)
print(ans) # 가장 큰 사이즈 출력 