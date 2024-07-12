# 스타트링크
# F: 전체 건물의 층 수, S: 현재, G: 목표 지점 

from collections import deque

F, S, G, U, D = map(int, input().split())

chk = [0] * (F+1)

def is_valid_coord(x):
    return 0 < x <= F

def bfs(now):
    dq = deque()
    dq.append(now)
    chk[now] = 1 
    
    while dq:
        now = dq.popleft()
        
        if now == G:
            return chk[now] - 1 
        
        else:
            for nxt in (now+U, now-D):
                if is_valid_coord(nxt) and not chk[nxt]:
                    chk[nxt] = chk[now] + 1 
                    dq.append(nxt)
    
    return 'use the stairs'

print(bfs(S))