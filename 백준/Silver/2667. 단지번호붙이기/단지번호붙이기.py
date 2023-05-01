# 단지번호붙이기 

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_board(y, x):
    return 0<=y<N and 0<=x<N

def dfs(y,x,d):
    board[y][x] = 0
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_board(ny, nx) and board[ny][nx] == 1:
            d = dfs(ny, nx, d+1)
                
    return d 

ans = 0 # 총 단지수       
res = [] # 단지내 집의 수 

for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            ans += 1 
            num = dfs(y, x, 1)
            res.append(num)
       
print(ans)  
for i in sorted(res):
    print(i)
