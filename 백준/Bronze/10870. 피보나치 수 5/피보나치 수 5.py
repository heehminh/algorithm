N = int(input())

if N == 0:
    print(0)
    exit()

dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])