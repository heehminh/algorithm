# DFS와 BFS 
from collections import deque

N, M, V = map(int, input().split())

# 인접행렬 
adj = [[0] * (N+1) for _ in range(N+1)]

# 간선 체크
for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1 
    
# 정답 배열 
dfs_ans = []
bfs_ans = []

# 체크 배열 
dfs_chk = [0] * (N+1)
bfs_chk = [0] * (N+1)

# dfs, 재귀 
def dfs(now):
    dfs_chk[now] = 1 
    dfs_ans.append(now)
    
    for nxt in range(N+1):
        if adj[now][nxt] == 1 and not dfs_chk[nxt]:
            dfs(nxt)

dfs(V)
print(*dfs_ans)

# bfs, 큐 
def bfs(now):
    dq = deque()
    bfs_chk[now] = 1
    dq.append(now)
    
    while dq:
        now = dq.popleft()
        bfs_ans.append(now)
        
        for nxt in range(N+1):
            if adj[now][nxt] == 1 and not bfs_chk[nxt]:
                dq.append(nxt)
                bfs_chk[nxt] = 1

bfs(V)
print(*bfs_ans)