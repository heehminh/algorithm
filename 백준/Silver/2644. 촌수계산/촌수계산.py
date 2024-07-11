# 촌수계산

N = int(input())
x, y = map(int, input().split())
M = int(input())

adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u][v] = adj[v][u] = 1
    
chk = [False] * (N+1)
res = []

def dfs(now, ans):
    chk[now] = True 
    
    if now == y:
        res.append(ans+1)
        return 
    
    for nxt in range(N+1):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True 
            dfs(nxt, ans+1)
    
dfs(x, 0)

if res:
    print(res.pop()-1)
else:
    print(-1)
