N, K = map(int, input().split())
S = list(map(int, input().split()))

start = 0
odd = 0
ans = 0 

for end in range(N):
    if S[end] % 2 == 1:
        odd += 1 
    
    while odd > K:
        if S[start] % 2 == 1:
            odd -= 1 
        start += 1 
    
    ans = max(ans, (end-start+1) - odd)

print(ans)