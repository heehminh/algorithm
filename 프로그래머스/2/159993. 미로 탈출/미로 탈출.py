from collections import deque 

def bfs(start, end, maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    
    chk = [[False] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == start:
                sy, sx = i, j
                
            elif maps[i][j] == end:
                ey, ex = i, j
    
    def is_valid_coord(y,x):
        return 0 <= y < N and 0 <= x < M

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

# S -> L / L -> E 
def solution(maps):
    to_lever = bfs('S', 'L', maps)
    to_end = bfs('L', 'E', maps)
    
    if to_lever != -1 and to_end != -1:
        return to_lever + to_end 
    
    return -1 
    