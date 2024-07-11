# 단지번호붙이기
# 연결요소의 개수(ans), 각 연결요소에 해당하는 개수(res)
from collections import deque 

N = int(input())

board = [list(input()) for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

ans = 0 # 총 단지수 
res = [] # 단지내 집의 수 

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    d = 1 
    
    while dq:
        x, y = dq.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if is_valid_coord(ny, nx) and board[nx][ny] == '1':
                dq.append((nx, ny))
                board[nx][ny] = '0'
                d += 1 
                
    return d 
    
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            board[i][j] = '0'
            num = bfs(i, j)
            ans += 1 
            res.append(num)

print(ans)

for num in sorted(res):
    print(num)
