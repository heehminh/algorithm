from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y, x): # 범위를 벗어나지 않는 좌표인지 확인 
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True 
    dq = deque()
    dq.append((0, 0, 1)) # y, x, 몇칸을 밟았는지 
    while dq:
        y, x, d = dq.popleft() # 현재칸의 위치를 나타내는 좌표
        
        if y == N-1 and x == M-1:
            return d
        
        nd = d + 1 
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and chk[ny][nx] == False:
                # 조건) 
                # 1. ny, nx가 범위를 벗어나지 않는 좌표인지
                # 2. board에 존재하는지
                # 3. 방문하지 않았는지 
                chk[ny][nx] = True 
                dq.append((ny, nx, nd))

print(bfs())