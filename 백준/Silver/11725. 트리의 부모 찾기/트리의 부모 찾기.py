import sys 
sys.setrecursionlimit(10**9) 

N = int(sys.stdin.readline())

adj = [[] for _ in range(N+1)]
chk = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
    
def dfs(now):
    for nxt in adj[now]:
        if not chk[nxt]:
            chk[nxt] = now 
            dfs(nxt)
            
dfs(1)

for i in range(2, N+1):
    print(chk[i])
