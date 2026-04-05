# 1954. 달팽이 숫자
T = int(input())
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(i, j):
    return 0 <= i < N and 0 <= j < N

for count in range(T):
    N = int(input())
    ans = [[0] * N for _ in range(N)]

    y, x, cnt, dr = 0, 0, 1, 0
    ans[y][x] = cnt
    cnt += 1

    while cnt <= N*N:
        ny = dy[dr] + y
        nx = dx[dr] + x

        if is_valid_coord(ny, nx) and ans[ny][nx] == 0:
            y, x = ny, nx
            ans[y][x] = cnt
            cnt += 1
        else:
            dr = (dr+1)%4

    print("#{}".format(count+1))
    for lst in ans:
        print(*lst)