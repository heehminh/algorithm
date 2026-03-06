from collections import deque
import sys
input = sys.stdin.readline 

N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

chk = [0] * (N+1)

res = []

def bfs(now, ans):
    dq = deque()
    dq.append((now, ans))
    chk[now] = True 
    
    while dq: 
        now, ans = dq.popleft()
        
        if ans == K:
            res.append(now)
        
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True 
                dq.append((nxt, ans+1))
                
bfs(X,0)

if res:
    for item in sorted(res):
        print(item)
else:
    print(-1)