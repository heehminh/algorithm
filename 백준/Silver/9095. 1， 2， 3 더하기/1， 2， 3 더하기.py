T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    
    if N == 1: 
        ans = 1
    
    if N == 2:
        ans = 2 
    
    if N == 3:
        ans = 4

    if ans != 0:
        print(ans)
    
    else:
        dp = [0] * (N+1)
        dp[1] = 1
        dp[2] = 2 # 2, 1+1
        dp[3] = 4 # 3, 2+1, 1+2, 1+1+1
        
        for i in range(4, N+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        print(dp[N])