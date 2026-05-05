def solution(n, computers):
    answer = 0
    
    chk = [False] * n 
    
    def dfs(now):
        chk[now] = True 
        for nxt in range(n):
            if computers[now][nxt] == 1 and not chk[nxt]:
                chk[nxt] = True 
                dfs(nxt)
        
    
    for i in range(n):
        if not chk[i]:
            chk[i] = True 
            answer += 1 
            dfs(i)
    
    return answer