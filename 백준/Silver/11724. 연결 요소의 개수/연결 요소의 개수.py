# 연결 요소의 개수 
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    # 무향그래프 
    adj[u][v] = adj[v][u] = 1 
    
chk = [0] * (N+1)
ans = 0 

def dfs(now):
    chk[now] = 1  # 체크 
    
    for nxt in range(1, N+1):
        if adj[now][nxt] == 1 and not chk[nxt]:
            dfs(nxt)
    
for i in range(1, N+1):
    if not chk[i]:
        ans += 1 
        dfs(i)
        
print(ans)