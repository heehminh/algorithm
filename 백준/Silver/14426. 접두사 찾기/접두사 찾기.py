import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
prefix_set = set()

for i in range(N):
    c = ''
    for char in list(arr[i]):
        c += char
        prefix_set.add(c)

ans = 0 
for _ in range(M):
    if input().rstrip() in prefix_set:
        ans += 1 

print(ans)