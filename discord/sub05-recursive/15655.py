N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

chk = [False] * N
res = []

def dfs(start):
    if len(res) == M:
        print(*res)
        return

    for nxt in range(start, N):
        if not chk[nxt]:
            chk[nxt] = True
            res.append(arr[nxt])

            dfs(nxt)

            chk[nxt] = False
            res.pop()

dfs(0)