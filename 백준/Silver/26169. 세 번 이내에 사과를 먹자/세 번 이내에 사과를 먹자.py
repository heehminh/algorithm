# 세 번 이내에 사과를 먹자
import sys  
sys.setrecursionlimit(10**6)

board = [list(map(int, input().split())) for _ in range(5)]

r, c = map(int, input().split())

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_not_valid_coord(y, x):
    return y > 4 or x > 4 or y < 0 or x < 0

bool = False 

def dfs(y, x, depth, ans):
    global bool
    ans = ans 
    
    if is_not_valid_coord(y, x) or depth > 3:
        return  
    
    if board[x][y] == -1: # 지뢰 
        return 
    
    if board[x][y] == 1: 
        ans += 1 
        
    tmp = board[x][y]
    board[x][y] = -1 
    
    ## 추가적인 재귀 방지 ## 
    if ans == 2:
        # 사과 2개를 먹음
        bool = True 
        return 
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        
        dfs(ny, nx, depth+1, ans)
    
    # 백트래킹: 원래대로 돌려놓음
    board[x][y] = tmp

dfs(c, r, 0, 0) # y, x, depth, ans

if bool:
    print(1)
else:
    print(0)