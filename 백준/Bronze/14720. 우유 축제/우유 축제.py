# 0: 딸기, 1: 초코, 2: 바나나
# 0 > 1 > 2 > 0

N = int(input())
arr = list(map(int, input().split()))
ans = 0
current = -1 

for i in range(N):
    if arr[i] == (current+1) % 3:
        ans += 1 
        current += 1 
        
print(ans)