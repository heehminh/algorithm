# 유기농 배추 
# 연결요소의 개수 

# 체크 배열 사용 X 
# 방문한 노드는 방문 처리 

from collections import deque

T = int(input())

for _ in range(T):

    N, M, K = map(int, input().split()) # 가로, 세로, 배추의 개수

    board = [[0] * N for _ in range(M)] # board[x][y]

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
        
    ans = 0 

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    def is_valid_coord(y, x):
        return 0 <= y < M and 0 <= x < N

    def bfs(y, x):
        dq = deque()
        dq.append((y, x))
        
        while dq:
            y, x = dq.popleft()
            
            if y == M-1 and x == N-1:
                return 
            
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                
                if is_valid_coord(ny, nx) and board[ny][nx] == 1:
                    dq.append((ny, nx))
                    # 칸 방문 처리 
                    board[ny][nx] = 0 
        return

    for x in range(N):
        for y in range(M):
            if board[y][x] == 1:
                bfs(y, x)
                ans += 1 
                
    print(ans)