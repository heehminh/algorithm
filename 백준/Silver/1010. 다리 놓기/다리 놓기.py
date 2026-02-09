T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    if M == N:
        print(1)
    
    else:
        dp = [0] * M
        dp[0] = 1
        
        for i in range(1, M):
            dp[i] = dp[i-1] * (i+1)
        
        ans = int(dp[M-1] / (dp[N-1] * dp[M-N-1])) # mCn
        print(ans)