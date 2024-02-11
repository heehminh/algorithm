N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]

# 간선 표시 
for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1][b-1] = adj[b-1][a-1] = 1 
    
ans = 0 # 연결요소의 개수 
chk = [False] * N # 체크 배열 

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and chk[nxt]==False:
            chk[nxt] = True 
            dfs(nxt)

for i in range(N):
    if chk[i] == False:
        ans += 1 
        chk[i] = True 
        dfs(i)
        
print(ans)