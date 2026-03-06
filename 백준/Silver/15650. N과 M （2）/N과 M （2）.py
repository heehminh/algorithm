N, M = map(int, input().split())

chk = [False] * (N+1)
res = []

def dfs():
    if len(res) == M:
        print(*res)
        return 
    
    for nxt in range(1, N+1):
        if not chk[nxt] and (not res or nxt > res[-1]):
            chk[nxt] = True 
            res.append(nxt)
            
            dfs()
            
            res.pop()
            chk[nxt] = False 

dfs()