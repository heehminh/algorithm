from collections import deque 

def bfs(start, end, maps):
    answer = 0 
    
    N = len(maps)
    M = len(maps[0])
    
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    
    def is_valid_coord(y, x):
        return 0 <= y < N and 0 <= x < M
    
    chk = [[False] * M for _ in range(N)]
    
    # start, end 설정 
    sy = sx = ey = ex = 0
    
    for y in range(N):
        for x in range(M):
            if maps[y][x] == start:
                sy, sx = y, x 
            elif maps[y][x] == end:
                ey, ex = y, x 
    
    # bfs 
    dq = deque()
    dq.append((sy, sx, 0))
    
    while dq:
        y, x, d = dq.popleft()
        
        if y == ey and x == ex:
            return d 
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if is_valid_coord(ny, nx) and not chk[ny][nx] and maps[ny][nx] != 'X':
                chk[ny][nx] = True 
                dq.append((ny, nx, d+1))
    
    return -1 

def solution(maps):
    # S -> L / L -> E 
    
    to_lever = bfs('S', 'L', maps)
    to_exit = bfs('L', 'E', maps)
    
    if to_lever != -1 and to_exit != -1:
        return to_lever + to_exit 
    
    return -1 