from collections import deque

N, Q = map(int, input().split())
arr = [[0] * N for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < N

def arr_input():
    sx, sy, ex, ey = map(int, input().split())
    for y in range(sy, ey):
        for x in range(sx, ex):
            arr[y][x] = n

def bfs(chk, sy, sx):
    dq = deque()
    sn = arr[sy][sx]
    rlst = []

    dq.append((sy, sx))
    chk[sy][sx] = sn
    rlst.append(sn)
    rlst.append([sy, sx])

    while dq:
        y, x = dq.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny, nx) and chk[ny][nx] == 0 and arr[ny][nx] == sn:
                chk[ny][nx] = sn
                dq.append((ny, nx))
                rlst.append([ny, nx])

    return rlst

def group():
    chk = [[0] * N for _ in range(N)]
    glst = []

    for sy in range(N):
        for sx in range(N):
            if not chk[sy][sx] and arr[sy][sx] > 0:
                tlst = bfs(chk, sy, sx)
                glst.append(tlst)
    return glst

def del_sort(glst):
    # 미생물 번호 2개 이상 삭제
    del_set = set()
    for i in range(len(glst)-1):
        for j in range(i+1, len(glst)): # 가능한 2개를 선택하는 모든 조합
            if glst[i][0] == glst[j][0]:
                del_set.add(i)
                del_set.add(j)

    for i in range(len(glst)-1, -1, -1):
        if i in del_set:
            glst.pop(i)

    # 정렬 (크기순, 오래된순)
    glst.sort(key=lambda x: (-len(x), x[0]))

    # 그룹 내 좌표를 (0,0) 기준의 상대좌표로 저장
    for lst in glst:
        # 1. y, x 최소합 구하기 => my, mx
        # 2. 모든 좌표에서 -my, -mx
        my, mx = N, N
        for cy, cx in lst[1:]:
            my = min(my, cy)
            mx = min(mx, cx)

        for idx in range(1, len(lst)):
            lst[idx][0] -= my
            lst[idx][1] -= mx

    return glst

def check(arr, lst):
    # 최소열 -> 최소행 기준으로 배치가능한지 체크후 기준좌표 리턴 (불가능시 -1, -1)
    for sx in range(N):
        for sy in range(N):
            for cy, cx in lst:
                ny, nx = sy + cy, sx + cx
                if ny >= N or nx >= N or arr[ny][nx] != 0:
                    break
            else:
                return sy, sx
    return -1, -1

def move(glst):
    narr = [[0] * N for _ in range(N)]

    for lst in glst:
        sn = lst[0]
        sy, sx = check(narr, lst[1:])
        if (sy, sx) != (-1, -1):
            for cy, cx in lst[1:]:
                narr[sy+cy][sx+cx] = sn

    return narr

def bfs_adj(w, sy, sx):
    dq = deque()
    dq.append((sy, sx))
    w[sy][sx] = True
    cnt = 1

    while dq:
        cy, cx = dq.popleft()

        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if is_valid_coord(ny, nx) and not w[ny][nx] and arr[ny][nx] == arr[cy][cx]:
                dq.append((ny, nx))
                w[ny][nx] = True
                cnt += 1

    return cnt

def bfs_score(chk, sy, sx):
    # 미방문 & 같은 세포 -> my_cnt
    # 미방문 & 다른 세포 -> cnts, 방문 표시 (w)
    dq = deque()
    dq.append((sy, sx))
    chk[sy][sx] = True
    w = [[0] * N for _ in range(N)]

    my_cnt = 1
    cnts = []

    while dq:
        cy, cx = dq.popleft()

        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if is_valid_coord(ny, nx) and chk[ny][nx] == 0:
                if arr[ny][nx] == arr[sy][sx]:
                    dq.append((ny, nx))
                    chk[ny][nx] = True
                    my_cnt += 1
                elif arr[ny][nx] > 0 and w[ny][nx] == 0:
                    tcnt = bfs_adj(w, ny, nx)
                    cnts.append(tcnt)

    ans = 0
    for cnt in cnts:
        ans += (my_cnt * cnt)

    return ans

def score(arr):
    ans = 0
    chk = [[0] * N for _ in range(N)]

    for sy in range(N):
        for sx in range(N):
            if not chk[sy][sx] and arr[sy][sx] > 0:
                t = bfs_score(chk, sy, sx)
                ans += t

    return ans


for n in range(1, Q+1):
    # [1] 입력: 기존 미생물 덮어씀
    arr_input()

    # [2] 그룹 나누기: glst = [미생물번호, (y1, x1), (y2, x2), ..]
    glst = group()

    # [3] 쪼개진 개체 삭제 및 정렬 (크기, 오래된: 미생물 번호가 작은)
    glst = del_sort(glst)
    # [4] 재배치
    arr = move(glst)

    # [5] 점수 계산
    ans = score(arr)
    print(ans)