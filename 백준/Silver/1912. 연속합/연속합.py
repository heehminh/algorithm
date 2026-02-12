N = int(input())
arr = list(map(int, input().split()))

cur = arr[0]
ans = arr[0]

for i in range(1, N):
    cur = max(arr[i], cur+arr[i])
    ans = max(ans, cur)

print(ans)