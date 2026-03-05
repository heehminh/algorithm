from collections import deque 
import sys 
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    I = int(input())
    
    dy = (1, 2, 2, 1, -1, -2, -2, -1)
    dx = (-2, -1, 1, 2, -2, -1, 1, 2)

    def is_valid_coord(y, x):
        return 0 <= y < I and 0 <= x < I 
    
    def bfs(y, x):
        chk = [[False] * I for _ in range(I)]
        chk[y][x] = True 
        
        dq = deque()
        dq.append((y, x, 0))
        
        while dq:
            y, x, d = dq.popleft()
            
            if y == ey and x == ex:
                return d
            
            for k in range(8):
                ny = y + dy[k]
                nx = x + dx[k]
                
                if is_valid_coord(ny, nx) and not chk[ny][nx]:
                    chk[ny][nx] = True 
                    dq.append((ny, nx, d+1))
    
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    
    if sy == ey and sx == ex:
        print(0)
    else:
        print(bfs(sy, sx))