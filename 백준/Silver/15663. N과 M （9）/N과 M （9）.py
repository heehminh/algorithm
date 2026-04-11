# N개의 자연수 중에서 M개를 고른 수열
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = []
chk = [False] * N
res = set()

def dfs():
    if len(ans) == M:
        res.add(tuple(ans))
        return

    for nxt in range(len(arr)):
        if not chk[nxt]:
            chk[nxt] = True
            ans.append(arr[nxt])

            dfs()

            ans.pop()
            chk[nxt] = False

dfs()

for x in sorted(res):
    print(*x)