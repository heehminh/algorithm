# 백준 2178 미로탐색
# 길찾기 알고리즘, 최단거리 -> BFS (큐로 구현)
# (1,1) -> (N,M)
# 다시 풀어보자!!!! 

import sys 
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline() for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True 
    dq = deque()
    dq.append((0, 0, 1)) # y, x, 횟수
    while dq:
        y, x, d = dq.popleft()
        
        # (N, M)에 도착했을 때 
        # 항상 도착위치로 이동할 수 있는 경우만 
        # 입력으로 주어진다는 조건이 있기 때문에
        # 다음과 같은 출력이 가능함 
        if y == N-1 and x == M-1:
            return d # 총 횟수 

        nd = d+1
        for k in range(4): # dy, dx가 갈 수 있는 경우의 수
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                # 이동을 했을 때 이동한 값이 board를 벗어나지 않아야 함
                # 이동한 값이 '1'이여서 그 곳을 지나갈 수 있어야 함
                # 한 번 지나간 곳이 아니여야 함 
                dq.append((ny, nx, nd))
                    
print(bfs())                