# 양 한마리... 양 두마리...
# #: 1, .: 0

from collections import deque

T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]

    ans = 0

    dy = (1, 0, -1, 0)
    dx = (0, 1, 0, -1)

    def is_valid_coord(y, x):
        return 0 <= y < W and 0 <= x < H

    def bfs(y, x):    
        dq = deque()
        dq.append((y, x))    
        
        while dq:
            y, x = dq.popleft()
            
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                
                if is_valid_coord(ny, nx) and board[nx][ny] == '#':
                    dq.append((ny, nx))
                    board[nx][ny] = '.'

    for i in range(H):
        for j in range(W):
            if board[i][j] == '#':
                board[i][j] = '.'
                bfs(j, i) # y, x
                ans += 1 
                
    print(ans)