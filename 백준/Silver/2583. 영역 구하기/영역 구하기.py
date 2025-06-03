import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split()) # y,x 
board = [[1]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[y][x] = 0 

ans = 0 # 연결요소의 개수 
res = []

chk = [[False]*N for _ in range(M)]

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

def is_valid_coord(y,x):
    return 0 <= y < M and 0 <= x < N

def dfs(y,x):
    cnt = 1 
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if is_valid_coord(ny, nx) and board[ny][nx] == 1 and not chk[ny][nx]:
            chk[ny][nx] = True 
            cnt += dfs(ny, nx)
    return cnt 

for y in range(M):
    for x in range(N):
        if not chk[y][x] and board[y][x] == 1:
            chk[y][x] = True 
            ans += 1
            cnt = dfs(y,x)
            res.append(cnt)

print(ans)
print(*sorted(res))