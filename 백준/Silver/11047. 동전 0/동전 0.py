N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = 0 # 동전 개수 

for i in range(len(arr)):
    idx = len(arr)-i-1
    if K //  arr[idx] > 0:
        ans += K // arr[idx]
        K %= arr[idx]

print(ans)