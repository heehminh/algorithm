from collections import deque

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호 
N, M, V = map(int, input().split())

adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1][b-1] = adj[b-1][a-1] = 1 
   
chk_dfs = [False] * N 

dfs_result = []

def dfs(now):
    chk_dfs[now] = True 
    dfs_result.append(now+1)

    for nxt in range(N):
        if adj[now][nxt] and not chk_dfs[nxt]:
            dfs(nxt)
    
dfs(V-1)
print(*dfs_result)

chk_bfs = [False] * N 
bfs_result = []

dq = deque()

def bfs(now):
    dq = deque()
    chk_bfs[now] = True 
    dq.append(now)

    while dq:
        now = dq.popleft()
        bfs_result.append(now+1)
        
        for nxt in range(N):
            if adj[now][nxt] and not chk_bfs[nxt]:
                dq.append(nxt)
                chk_bfs[nxt] = True 
                
bfs(V-1)
print(*bfs_result)