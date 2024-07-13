# 토마토 
# 익은 토마토, 안 익은 토마토 
# 보관 후 하루가 직하면, 익은 토마토의 인접한 곳에 있는 토마토가 익음
# 인접: 위, 아래, 왼, 오, 앞, 뒤 (6)
# 며칠이 지나면 다 익게 되는지 (최소탐색 => BFS)

from collections import deque

M, N, H = map(int, input().split()) 

board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = (1, 0, 0, -1, 0, 0)
dy = (0, 1, 0, 0, -1, 0)
dz = (0, 0, 1, 0, 0, -1)

def is_valid_coord(x, y, z):
    return 0 <= x < N and 0 <= y < M and 0 <= z < H

def bfs():
    while dq:
        x, y, z = dq.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            
            if is_valid_coord(nx, ny, nz) and board[nz][nx][ny] == 0: 
                board[nz][nx][ny] = board[z][x][y] + 1 # 영향
                dq.append((nx, ny, nz))

dq = deque() # 모든 익은 토마토의 위치를 큐에 담음 

for z in range(H):
    for x in range(N):
        for y in range(M):
            if board[z][x][y] == 1: # 익은 토마토 
                dq.append((x, y, z))

bfs()
is_completed = True  
ans = 0 # 며칠 걸리는지 

for z in range(H):
    for x in range(N):
        for y in range(M):
            if board[z][x][y] == 0: 
                is_completed = False # 하나라도 안익은 토마토가 있다면
            ans = max(ans, board[z][x][y])

if not is_completed:
    print(-1)
else:
    print(ans-1)