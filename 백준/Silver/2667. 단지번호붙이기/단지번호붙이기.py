# dfs

N = int(input())
board = [input() for _ in range(N)]
res = []

chk = [[False]*N for _ in range(N)]

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < N

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def dfs(y,x):
    global cnt 
    chk[y][x] = True 
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if is_valid_coord(ny,nx) and not chk[ny][nx] and board[ny][nx] == '1':
            chk[ny][nx] = True 
            res[cnt-1] += 1 
            dfs(ny, nx)
    

cnt = 0 
for y in range(N):
    for x in range(N):
        if not chk[y][x] and board[y][x] == '1':
            chk[y][x] = True 
            cnt += 1 
            res.append(1)
            dfs(y,x)

print(len(res))

for row in sorted(res):
    print(row)