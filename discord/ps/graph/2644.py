import sys 
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
adj = [[0] * (N+1) for _ in range(N+1)]

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1 
    
chk = [False] * (N+1)
res = -1

def dfs(now, ans):
    global res 
    chk[now] = True 
    
    if now == b:
        res = ans 
        return 

    for nxt in range(N+1):
        if not chk[nxt] and adj[now][nxt]:
            dfs(nxt, ans+1)

dfs(a, 0)
print(res)