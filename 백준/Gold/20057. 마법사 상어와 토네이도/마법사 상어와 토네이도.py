# 20057. 마법사 상어와 토네이토
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 좌, 하, 우, 상
dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

mul = [2, 10, 7, 1, 5, 10, 7, 1, 2, 0]
ay = [[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0],
      [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]]
ax = [[0, -1, 0, 1, -2, -1, 0, 1, 0, -1],
      [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

cy = cx = N//2
ans = cnt = flag = dr = 0
cnt_mx = 1

while (cy,cx) != (0,0):
    cy = cy + dy[dr]
    cx = cx + dx[dr]

    # 1. 한칸이동
    # cy, cx: 기준 좌표 중심으로 모래량 계산 추가, 범위 밖이면 ans에 추가
    if arr[cy][cx] > 0:
        val = arr[cy][cx]
        arr[cy][cx] = 0
        sm = 0

        for i in range(10):
            ny = cy + ay[dr][i]
            nx = cx + ax[dr][i]
            t = (val * mul[i]) // 100

            if i == 9:
                t = val-sm

            if is_valid_coord(ny, nx):
                arr[ny][nx] += t
            else:
                ans += t
            sm += t

    cnt += 1
    if cnt == cnt_mx:
        cnt = 0
        dr = (dr+1) % 4

        if flag == 0:
            flag = 1
        else:
            flag = 0
            cnt_mx += 1
print(ans)