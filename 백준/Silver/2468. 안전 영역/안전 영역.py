'''
물에 잠기지 않는 안전한 영역의 최대 개수, 최대 높이 값에 따른 

1. 최대 높이가 4일 때 구해보기 
2. for 문 돌려서 값 array에 넣고 return max 
'''

from collections import deque

N = int(input())

adj = [[0] * N for _ in range(N)]

for i in range(N):
    adj[i] = list(map(int, input().split()))

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def bfs(x, y): 
    dq = deque()
    dq.append((x, y))
    
    while dq:
        x, y = dq.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if is_valid_coord(ny, nx) and not chk[nx][ny] and adj[nx][ny] > num:
                chk[nx][ny] = True   
                dq.append((nx, ny))           

res = 1

for num in range(1, 101): 
    ans = 0
    chk = [[False] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if not chk[i][j] and adj[i][j] > num:
                ans += 1
                bfs(i, j)
                       
    res = max(ans, res)
            
print(res)