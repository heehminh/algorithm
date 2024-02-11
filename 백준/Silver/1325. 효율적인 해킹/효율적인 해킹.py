from collections import deque
import sys 

N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]

# A가 B를 신뢰한다. 노드를 표현하면 B는 A의 부모이다.
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a) # 연결리스트 
    
def bfs(now):
    dq = deque()
    dq.append(now)
    cnt = 0 
    
    chk = [False] * (N+1)
    chk[now] = True 
    
    while dq:
        current = dq.popleft()
        for nxt in adj[current]:
            if not chk[nxt]:
                chk[nxt] = True 
                dq.append(nxt)
                cnt += 1 
    return cnt 

res = []
for now in range(1, len(adj)):
    res.append(bfs(now))
    
for i in range(len(res)):
    if max(res) == res[i]:
        print(i+1, end=" ")