from collections import deque 
import sys 
input = sys.stdin.readline

R, C = map(int, input().split()) # y, x 
boards = [list(input().rstrip()) for _ in range(R)]
fire_times = [[1000000000] * C for _ in range(R)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < R and 0 <= x < C 

q1 = deque()
start_y, start_x = 0, 0

# 불이 몇 분 뒤에 붙는지 
for y in range(R):
    for x in range(C):
        if boards[y][x] == 'F':
            fire_times[y][x] = 0 
            q1.append((y, x, 0))
        if boards[y][x] == 'J':
            boards[y][x] = '.'
            start_y = y
            start_x = x 

chk = [[False] * C for _ in range(R)]
chk[y][x] = True 

while q1:
    y, x, d = q1.popleft()
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if is_valid_coord(ny, nx) and not chk[ny][nx] and boards[ny][nx] != '#':
            fire_times[ny][nx] = d+1 
            chk[ny][nx] = True 
            q1.append((ny, nx, d+1))

def bfs(y, x, d):
    chk = [[False] * C for _ in range(R)]
    chk[y][x] = True 
    
    dq = deque()
    dq.append((y, x, d))
    
    while dq:
        y, x, d = dq.popleft()
        
        if y == 0 or y == R-1 or x == 0 or x == C-1:
            return d+1 

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny, nx) and not chk[ny][nx] and boards[ny][nx] == '.' and fire_times[ny][nx] > d+1:
                chk[ny][nx] = True 
                dq.append((ny, nx, d+1))
    
    return 'IMPOSSIBLE'

print(bfs(start_y, start_x, 0))