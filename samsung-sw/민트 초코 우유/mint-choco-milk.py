from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < N

def bfs(chk, sy, sx):
    dq = deque()
    food = farr[sy][sx]
    blst = []

    dq.append((sy, sx))
    chk[sy][sx] = food
    blst.append([-barr[sy][sx], sy, sx])

    while dq:
        cy, cx = dq.popleft()

        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if is_valid_coord(ny, nx) and chk[ny][nx] == 0 and farr[ny][nx] == food:
                dq.append((ny, nx))
                chk[ny][nx] = food
                blst.append([-barr[ny][nx], ny, nx])

    blst.sort()
    _, by, bx = blst[0]
    barr[by][bx] += len(blst)
    return by, bx

group_ord = {4:1, 2:1, 1:1, 3:2, 5:2, 6:2, 7:3}
def group():
     boss = []
     chk = [[0] * N for _ in range(N)]
     for i in range(N):
         for j in range(N):
             if chk[i][j] == 0:
                 ti, tj = bfs(chk, i, j)
                 food = farr[ti][tj] # 대표자 음식
                 # 신앙심 가장 큰 -> 행이 작은 -> 열이 작은
                 boss.append([group_ord[food], -barr[ti][tj], ti, tj])
     return boss

# def myprt():
#     for lst in barr:
#         print(*lst)
#     print("-"*20)
#     for lst in farr:
#         print(*lst)
#     print("="*20)

def move(blst):
    # 전파방법: 신앙심%4 -> 방향(0: 상, 1: 하, 2: 좌, 3: 우)
    # 간절함 = 신앙심 -1 (간절함이 0이 되거나, 격자밖으로 나가면 전파 종료)
    # 같은 음식이면 다음 칸 이동 (다른 음식이면 전파 진행)
    # 간절함: x, 신앙심: y인 경우
    # 1) x>y (강한전파): 동일음식 신봉, x=x-(y+1), y=y+1
    # 2) x<=y (약한전파): 전파음식추가 (비트), x=0, y=y+x
    # 전파당하면 방어상태, 당일에는 전파하지 X (전파는 받음)

    moved = set() # 전파당함
    for _, cn, cy, cx in blst:
        if (cy, cx) in moved:
            continue

        cn = -cn
        dry, drx = dy[cn%4], dx[cn%4]
        score = cn-1 # 간절함
        barr[cy][cx] = 1 # 대표자는 1의 값을 가짐
        food = farr[cy][cx]

        while True:
            # 범위 내 간절함이 0이 아닌 동안
            ny, nx = cy+dry, cx+drx
            if not is_valid_coord(ny, nx) or score <= 0:
                break

            # 전파
            if farr[ny][nx] != food:
                moved.add((ny, nx)) # 전파처리 -> 방어상태
                if score > barr[ny][nx]: # 강한전파
                    farr[ny][nx] = food
                    barr[ny][nx] += 1
                    score -= barr[ny][nx]
                else: # 약한전파
                    farr[ny][nx] |= food # 비트연산 or
                    barr[ny][nx] += score
                    break

            cy, cx = ny, nx

N, T = map(int, input().split())

tbl = {'T': 4, 'C': 2, 'M': 1}
farr = [list(input()) for _ in range(N)]
barr = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        farr[y][x] = tbl[farr[y][x]]

for _ in range(T):
    # [1] 대표자 리스트 (전파할 우선순위)
    # 단일 -> 이중 -> 삼중 / 신앙심큰 / 행작은 / 열작은
    blst = group()
    # myprt()

    # [2] 대표자 리스트 오름차순 정렬 후 전파 진행
    blst.sort()
    move(blst)

    # [3] 출력
    # 민초우(7), 민초(6), 민우(5), 초우(3), 우유(1), 초코(2), 민트(4)
    ans = [0]*7
    for idx, food in enumerate((7, 6, 5, 3, 1, 2, 4)):
        for i in range(N):
            for j in range(N):
                if farr[i][j] == food:
                    ans[idx] += barr[i][j]

    print(*ans)