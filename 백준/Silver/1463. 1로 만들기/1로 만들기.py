# 3. 1을 뺀다
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.

N = int(input())
dp = [0] * (N+1) # idx번째 숫자를 만드는데 필요한 최소연산수

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])