N, M = map(int, input().split())
res = []
chk = [False] * (N+1)

def dfs():
    if len(res) == M:
        print(*res)
        return 
    
    for nxt in range(1, N+1):
        if not chk[nxt]:
            chk[nxt] = True 
            res.append(nxt)
            dfs()
            
            res.pop() # 백 
            chk[nxt] = False 
    
dfs()