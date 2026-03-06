from collections import deque 
import sys
input = sys.stdin.readline 

R, C = map(int, input().split())
boards = [list(input().strip()) for _ in range(R)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < R and 0 <= x < C 

def bfs():
    chk = [[False] * C for _ in range(R)]
    
    dq = deque()

    for y in range(R):
        for x in range(C):
            if boards[y][x] == 'W':
                chk[y][x] = True 
                dq.append((y, x))
    
    while dq:
        y, x = dq.popleft()
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if is_valid_coord(ny, nx) and boards[ny][nx] == 'S':
                print(0)
                exit()
            
            if is_valid_coord(ny, nx) and not chk[ny][nx] and boards[ny][nx] == '.':
                boards[ny][nx] = 'D'
                
bfs()

print(1)
for row in boards:
    print(''.join(row))
