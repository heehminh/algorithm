from collections import deque 
import sys 
input = sys.stdin.readline 

N = int(input())
boards = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
min_height = 101 

for row in boards:
    max_height = max(max(row), max_height)
    min_height = min(min(row), min_height)

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N 

res = [1]

def bfs(y, x, h):
    chk[y][x] = True 
    dq = deque()
    dq.append((y,x))
    
    while dq: 
        y, x = dq.popleft()
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if is_valid_coord(ny, nx) and not chk[ny][nx] and boards[ny][nx] > h:
                chk[ny][nx] = True 
                dq.append((ny, nx))

ans = 1 

for h in range(min_height, max_height+1): 
    ans = 0 
    chk = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not chk[y][x] and boards[y][x] > h:
                ans += 1 
                bfs(y, x, h)
    res.append(ans)

print(max(res))

