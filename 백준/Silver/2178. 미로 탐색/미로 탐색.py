# 최단거리 BFS 
import sys 
from collections import deque 
input = sys.stdin.readline

N, M = map(int, input().split()) 
board = [input() for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y <= N-1 and 0 <= x <= M-1

def bfs():
    chk = [[False] * M for _ in range(N)]
    dq = deque()
    chk[0][0] = True 
    dq.append((0, 0, 1)) # y, x, d 
    
    while dq:
        y, x, d = dq.popleft()
        
        # 종료조건 
        if y == N-1 and x == M-1:
            return d 
        
        nd = d+1 
        
        for k in range(4):
            ny = dy[k] + y 
            nx = dx[k] + x 
            
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = 1 
                dq.append((ny, nx, nd))
                
print(bfs()) # d 