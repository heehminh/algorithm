def solution(n, computers):
    answer = 0
    
    chk = [False] * n 
    
    def dfs(now):
        chk[now] = True 
        
        for nxt in range(n):
            if not chk[nxt] and computers[now][nxt] == 1:
                chk[nxt] = True 
                dfs(nxt)
    
    for idx in range(n):
        if not chk[idx]:
            dfs(idx)
            answer += 1 
    
    return answer