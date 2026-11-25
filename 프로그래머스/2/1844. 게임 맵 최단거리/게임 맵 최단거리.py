from collections import deque 

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    def is_valid_coord(y,x):
        return 0 <= y < N and 0 <= x < M 
    
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    
    chk = [[False] * M for _ in range(N)]
    
    def bfs():
        dq = deque()
        chk[0][0] = True 

        dq.append((0, 0, 1))

        while dq:
            cy, cx, cd = dq.popleft()
            chk[cy][cx] = True 

            if cy == N-1 and cx == M-1:
                return cd 

            for k in range(4):
                ny = cy + dy[k]
                nx = cx + dx[k]

                if is_valid_coord(ny, nx) and not chk[ny][nx] and maps[ny][nx] == 1:
                    chk[ny][nx] = True 
                    dq.append((ny, nx, cd+1))
        
        return -1 
    
    return bfs()