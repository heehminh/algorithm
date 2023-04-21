# DFS와 BFS
import sys 
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split()) # 정점, 간선, 시작

# 인접행렬
adj = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1 

# 체크배열
chk_dfs = [False] * (N+1)

# DFS 
def dfs(now):
    chk_dfs[now] = 1 
    print(now, end =" ")
    
    for nxt in range(1, N+1):
        if adj[now][nxt] and not chk_dfs[nxt]:
            dfs(nxt)
   
# 체크배열
chk_bfs = [False] * (N+1) 
        
# BFS 
def bfs(now):
    dq = deque()
    dq.append(now)
    chk_bfs[now] = 1 
    
    while dq:
        now = dq.popleft()
        print(now, end =" ")
        
        for nxt in range(1, N+1):
            if adj[now][nxt] and not chk_bfs[nxt]:
                dq.append(nxt)
                chk_bfs[nxt] = 1 

dfs(V)
print()
bfs(V)