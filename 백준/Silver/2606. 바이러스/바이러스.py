N = int(input())
M = int(input())

adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1][b-1] = adj[b-1][a-1] = 1 

chk = [False] * N

def dfs(now):
    chk[now] = True 
    
    for nxt in range(N):
        if not chk[nxt] and adj[now][nxt]:
            dfs(nxt)

dfs(0)

print(chk.count(True) - 1)
