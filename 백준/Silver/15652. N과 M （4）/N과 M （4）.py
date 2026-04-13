N, M = map(int, input().split())

res = []

def dfs(start):
    if len(res) == M:
        print(*res)
        return

    for idx in range(start, N+1):
        res.append(idx)
        dfs(idx)
        res.pop()

dfs(1)