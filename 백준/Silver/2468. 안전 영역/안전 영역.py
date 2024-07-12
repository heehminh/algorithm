# 안전 영역 
# BFS
# N 이상을 1로, N 이하를 0으로 생각 
# 연결요소의 !최대! 개수 

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    
    while dq:
        x, y = dq.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if is_valid_coord(nx, ny) and not chk[nx][ny] and board[nx][ny] > height:
                chk[nx][ny] = True 
                dq.append((nx, ny))

res = 1 # 최댓값으로 업데이트

for height in range(1, 101): # N: 1~N까지 높이
    ans = 0 # 연결요소의 개수
    chk = [[False] * (N) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if not chk[i][j] and board[i][j] > height:
                ans += 1 
                bfs(i, j) # x, y
    
    res = max(res, ans)

print(res)