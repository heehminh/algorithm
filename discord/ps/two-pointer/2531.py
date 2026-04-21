import sys 
input = sys.stdin.readline 

N, D, K, C = map(int, input().split()) 
arr = [int(input()) for _ in range(N)]

chk = [0] * (D+1)
ans = 0 
kind = 0

for i in range(K):
    if not chk[arr[i]]:
        kind += 1 
    chk[arr[i]] += 1 

ans = kind
if not chk[C]:
    ans += 1 

for i in range(1, N):
    left = arr[i-1]
    right = arr[(i+K-1)%N]
    
    chk[left] -= 1 
    if not chk[left]:
        kind -= 1 
    
    if not chk[right]:
        kind += 1 
    chk[right] += 1 
    
    temp = kind
    if not chk[C]:
        temp += 1 
    
    ans = max(ans, temp)

print(ans)
