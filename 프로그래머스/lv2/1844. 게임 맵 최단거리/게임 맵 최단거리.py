from collections import deque 

def solution(maps):
    M = len(maps[0])
    N = len(maps)
    
    dy = (1, 0, -1, 0)
    dx = (0, 1, 0, -1)
    
    def is_valid_coord(y,x):
        return 0 <= y < N and 0 <= x < M 
    
    def bfs():
        chk = [[False] * M for _ in range(N)]
        chk[0][0] = True 
        
        dq = deque()
        dq.append((0, 0, 1)) # y, x, d 
        
        while dq:
            y, x, d = dq.popleft()
            
            if y == N-1 and x == M-1:
                return d 
            
            nd = d + 1
            
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                
                if is_valid_coord(ny, nx) and maps[ny][nx] == 1 and not chk[ny][nx]:
                    chk[ny][nx] = True 
                    dq.append((ny, nx, nd))
                    
        return -1 
    
    return bfs()