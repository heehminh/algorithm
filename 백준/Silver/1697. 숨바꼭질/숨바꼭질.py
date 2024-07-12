# 숨바꼭질 
# 최단거리 찾기: BFS 
from collections import deque

N, K = map(int, input().split())
M = 100000

chk = [0] * (M+1)

def is_valid_coord(x):
    return 0 <= x <= M

def bfs(now):
    dq = deque()
    dq.append(now)
    chk[now] = 1 
    
    while dq:
        now = dq.popleft()
        
        if now == K:
            return chk[now] - 1 

        else:
            for nxt in (now-1, now+1, 2*now):
                if is_valid_coord(nxt) and not chk[nxt]:
                    chk[nxt] = chk[now] + 1 
                    dq.append(nxt)

print(bfs(N))
