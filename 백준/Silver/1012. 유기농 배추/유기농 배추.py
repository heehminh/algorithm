import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < M 

def dfs(y,x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if is_valid_coord(ny, nx) and board[ny][nx] == 1 and not chk[ny][nx]:
            chk[ny][nx] = True 
            dfs(ny, nx)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    
    ans = 0 
    chk = [[False]*M for _ in range(N)]
        
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1 

    for y in range(N):
        for x in range(M):
            if not chk[y][x] and board[y][x] == 1:
                chk[y][x] = True 
                ans += 1 
                dfs(y, x)
                
    print(ans)