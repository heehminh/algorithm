# 바이러스 

N = int(input())
M = int(input())

adj = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    # 무향그래프
    adj[u][v] = adj[v][u] = 1 

ans = 0
chk = [0] * (N+1)

def dfs(now):
    global ans
    chk[now] = 1 
    
    for nxt in range(N+1):
        if adj[now][nxt] == 1 and not chk[nxt]:
            ans += 1 
            dfs(nxt)
    
dfs(1)
print(ans)