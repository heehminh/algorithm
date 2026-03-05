from collections import deque
import sys 
input = sys.stdin.readline 

M, N = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M 

def bfs():
    dq = deque()
    
    for y in range(N):
        for x in range(M):
            if boards[y][x] == 1:
                dq.append((y,x))
    
    while dq:
        y, x = dq.popleft()
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if is_valid_coord(ny, nx) and boards[ny][nx] == 0:
                boards[ny][nx] = boards[y][x] + 1 
                dq.append((ny, nx))

bfs()

ans = 1 
for row in boards:
    if 0 in row:
        print(-1)
        exit()
    ans = max(ans, max(row))

print(ans-1)