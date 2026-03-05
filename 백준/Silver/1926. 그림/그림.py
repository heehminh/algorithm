from collections import deque
import sys 

input = sys.stdin.readline

N, M = map(int, input().split())
boards = [list(input().split()) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M 

arr = [] # 넓이 배열 
chk = [[False] * M for _ in range(N)]

def bfs(y, x):
    cnt = 1 
    chk[y][x] = True 
    dq = deque()
    dq.append((y, x)) # y, x 
    
    while dq:
        y, x = dq.popleft()
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if is_valid_coord(ny, nx) and not chk[ny][nx] and boards[ny][nx] == '1':
                chk[ny][nx] = True 
                cnt += 1 
                dq.append((ny, nx))
    
    return cnt

cnt = 0 
for y in range(N):
    for x in range(M):
        if not chk[y][x] and boards[y][x] == '1':
            arr.append(bfs(y, x))

arr.sort()
print(len(arr))
print(arr[-1] if len(arr) > 0 else 0)