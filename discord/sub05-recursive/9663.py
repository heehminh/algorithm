def sol(k):
    global N, cnt

    if k == N:
        cnt += 1
        return

    for i in range(N):
        if not used_c[i] and not used_up[k + i] and not used_down[(N - 1) + k - i]:
            used_c[i] = True
            used_up[k + i] = True
            used_down[(N - 1) + k - i] = True
            sol(k + 1)
            used_c[i] = False
            used_up[k + i] = False
            used_down[(N - 1) + k - i] = False

N = int(input())
maps = [[0] * N for _ in range(N)]

used_c = [False] * N
used_up = [False] * (2 * (N - 1) + 1)
used_down = [False] * (2 * (N - 1) + 1)

cnt = 0

sol(0)
print(cnt)