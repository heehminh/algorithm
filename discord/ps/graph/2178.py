from collections import deque
import sys 

input = sys.stdin.readline

N, M = map(int, input().split())
boards = [input() for _ in range(N)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M 

chk = [[False] * M for _ in range(N)]

def bfs():
    dq = deque()
    dq.append((0, 0, 1)) # y, x, d
    chk[0][0] = True 
    
    while dq:
        y, x, d = dq.popleft()
        
        if y == N-1 and x == M-1:
            return d 
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if is_valid_coord(ny, nx) and not chk[ny][nx] and boards[ny][nx] == '1':
                chk[ny][nx] = True 
                dq.append((ny, nx, d+1))
                
    return -1

print(bfs()) 