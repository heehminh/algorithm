def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    dp[0] = [triangle[0][0]]
    
    for h in range(1, len(triangle)):
        dp[h][0] = dp[h-1][0] + triangle[h][0]
        dp[h][-1] = dp[h-1][-1] + triangle[h][-1]

        for i in range(1, len(triangle[h])-1):
            dp[h][i] = max(dp[h-1][i-1], dp[h-1][i]) + triangle[h][i]
    
    return max(dp[-1])