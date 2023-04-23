# 미로탐색
# 길찾기, 최단거리탐색 => BFS 
# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다

from collections import deque
import sys 

input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False] * M for _ in range(N)] 
    chk[0][0] = 1 
    dq = deque()
    dq.append((0, 0, 1)) # y, x, 몇칸을 지나왔는지
    while dq:
        y, x, d = dq.popleft()
        
        if y == N-1 and x == M-1:
            return d 
        
        nd = d + 1 
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k] 
            if is_valid_coord(ny, nx) and board[ny][nx] == "1" and not chk[ny][nx]:
                chk[ny][nx] = 1 
                dq.append((ny, nx, nd))
    
print(bfs())