# 미로 탐색: 길찾기 (최단거리탐색, BFS)
from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 채크 배열 
chk = [[False] * (M) for _ in range(N)]

# 움직일 수 있는 방향 
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 범위 체크: 유효한 좌표인지
def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    # 초기값 체크 
    chk[0][0] = True 
    
    dq = deque()
    dq.append((0, 0, 1)) # y, x, ans 
    
    while dq:
        y, x, d = dq.popleft()
        
        if y == N-1 and x == M-1:
            return d 
        
        nd = d + 1 
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            # 범위 체크
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True 
                dq.append((ny, nx, nd))

print(bfs())            