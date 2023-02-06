# 백준 11724번 연결 요소의 개수 
# 무향그래프
# N: 정점의 개수, M: 간선의 개수

import sys
N, M = map(int, sys.stdin.readline().split())

# 그래프를 담을 인접행렬
adj = [[0]*N for _ in range(N)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u-1][v-1] = adj[v-1][u-1] = 1
    
chk = [False] * N
ans = 0

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True 
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1 
        chk[i] = True
        dfs(i)

print(ans)