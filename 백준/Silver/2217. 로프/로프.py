N = int(input())
arr = [int(input()) for _ in range(N)]

ans = 0
arr.sort()

for i in range(len(arr)):
    ans = max(ans, arr[i] * (len(arr)-i))

print(ans)