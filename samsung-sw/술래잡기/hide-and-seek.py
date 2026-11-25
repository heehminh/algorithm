N, M, H, K = map(int, input().split())

# 도망자 좌표
# 좌:0, 우:1, 하:2, 상:3
arr = []
for _ in range(M):
    x, y, d = map(int, input().split())
    arr.append([x-1, y-1, d])

# 나무 좌표
tree = set()
for _ in range(H):
    x, y = map(int, input().split())
    tree.add((x-1, y-1))

# 좌 우 하 상
dy = (0, 0, 1, -1)
dx = (-1, 1, 0, 0)
opp = {0:1, 1:0, 2:3, 3:2}

# 상 우 하 좌
tdy = (-1, 0, 1, 0)
tdx = (0, 1, 0, -1)

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

ans = cnt = dr = flag = 0
val = 1 # 1: 안쪽 / -1: 바깥쪽
ty = tx = N // 2
cnt_mx = 1

for k in range(1, K+1):
    # [1] 도망자의 이동 (arr)
    for i in range(len(arr)):
        if abs(arr[i][0]-ty)+abs(arr[i][1]-tx) <= 3:
            ny = arr[i][0] + dy[arr[i][2]]
            nx = arr[i][1] + dx[arr[i][2]]
            if is_valid_coord(ny, nx):
                if (ny, nx) != (ty, tx):
                    arr[i][0], arr[i][1] = ny, nx
            else:
                nd = opp[arr[i][2]]
                ny = arr[i][0] + dy[nd]
                nx = arr[i][1] + dx[nd]
                if (ny, nx) != (ty, tx):
                    arr[i] = [ny, nx, nd]

    # [2] 술래의 이동
    cnt += 1
    ty = ty + tdy[dr]
    tx = tx + tdx[dr]

    if (ty, tx) == (0,0):
        cnt_mx, cnt, flag, val = N, 1, 1, -1
        dr = 2

    elif (ty, tx) == (N//2, N//2):
        cnt_mx, cnt, flag, val = 1, 0, 0, 1
        dr = 0

    else:
        if cnt == cnt_mx:
            cnt = 0
            dr = (dr+val) % 4

            if flag == 0:
                flag = 1
            else:
                flag = 0
                cnt_mx += val

    # [3] 도망자 잡기
    # 술래자리포함 3칸, 나무가 없는 도망자면 삭제
    tset = set((((ty, tx),
                 (ty+tdy[dr], tx+tdx[dr]),
                 (ty+tdy[dr]*2, tx+tdx[dr]*2))))

    for i in range(len(arr)-1, -1, -1):
        if (arr[i][0], arr[i][1]) in tset and (arr[i][0], arr[i][1]) not in tree:
            ans += k
            arr.pop(i)

    if not arr:
        break

print(ans)