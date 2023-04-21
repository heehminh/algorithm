# 백준 1012 유기농 배추 
# M: 배추밭의 가로길이
# N: 배추밭의 세로길이
# K: 배추가 심어져있는 위치의 개수
# X, Y (최대 M, N)

import sys 
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def is_valid_coord(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(x, y):
    dq = deque()
    dq.append((x,y))
    
    while dq: 
        x, y = dq.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if is_valid_coord(nx, ny) and board[nx][ny]:
                dq.append((nx, ny))
                board[nx][ny] = 0 # 방문
    return             
                
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1 
    
    ans = 0 
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                bfs(i, j)
                ans += 1 

    print(ans)
    



