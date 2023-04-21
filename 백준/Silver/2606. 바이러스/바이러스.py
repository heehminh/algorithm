# 바이러스
import sys 
input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1 
    
ans = 0 
chk = [False] * (N+1)

def dfs(now):
    chk[now] = 1 
    
    for nxt in range(1, N+1):
        if adj[now][nxt] and not chk[nxt]:
            dfs(nxt)

for i in range(1, N+1):
    if not chk[i] and i == 1:
        ans += 1 
        chk[i] = 1 
        dfs(i)
    
print(chk.count(1) -1)
