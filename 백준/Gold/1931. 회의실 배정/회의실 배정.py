N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: (x[1], x[0]))

start = arr[0][0]
end = arr[0][1]
ans = 1

for s, e in arr[1:]:
    if s >= end: 
        start = s 
        end = e 
        ans += 1 
        
print(ans)