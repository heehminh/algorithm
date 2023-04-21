# 백준 11724 연결 요소의 개수
# 인접행렬을 쓸 지, 인접리스트를 쓸 지
# N, M: 정점, 간선 (1 <= N <= 1000, 0 <= M <= N*(N-1)/2)
# NC2: N개 중에 서로 다른 정점 2개를 뽑느 경우의 수
# => 인접행렬을 사용한다 

import sys 

N, M = map(int, sys.stdin.readline().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, sys.stdin.readline().split()))
    adj[a][b] = adj[b][a] = 1

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