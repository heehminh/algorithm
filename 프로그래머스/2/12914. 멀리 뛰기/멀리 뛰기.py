def solution(n):
    answer = 0
    
    if n == 1:
        return 1 
    
    if n == 2:
        return 2 
    
    dp = [0] * (n+1)
    dp[1] = 1 # 1칸일때 1가지 
    dp[2] = 2 # 2칸일때 2가지 
    
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    
    return dp[-1] % 1234567