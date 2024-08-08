# 트리의 부모 찾기
# 1
# 6 4 
# 3 (2, 7)
# 5 
import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
chk = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(now):
    for nxt in adj[now]:
        if not chk[nxt]:
            chk[nxt] = now
            dfs(nxt)

dfs(1)

for i in range(2, N+1):
    # 부모 노드 출력 
    print(chk[i])