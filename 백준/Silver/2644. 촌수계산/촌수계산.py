# 촌수계산
# dfs 

N = int(input()) # 전체 사람의 수 
A, B = map(int, input().split())
M = int(input()) 
adj = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1 

result = []
chk = [False] * (N+1)

def dfs(now, ans):
    ans += 1 
    chk[now] = 1 
    
    if now == B:
        result.append(ans)
    
    for nxt in range(1, N+1):
        if adj[now][nxt] and not chk[nxt]:
            dfs(nxt, ans)
        
dfs(A, 0)
print(result[0]-1 if len(result)!=0 else -1)