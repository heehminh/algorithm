R, C = map(int, input().split())

boards = [list(input()) for _ in range(R)]
answers = [['.'] * C for _ in range(R)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y,x):
    return 0 <= y < R and 0 <= x < C 

sy, sx, ey, ex = 10, 10, 0, 0

for y in range(R):
    for x in range(C):
        if boards[y][x] == 'X':
            cnt = 0 
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                
                if not is_valid_coord(ny, nx):
                    cnt += 1 
                
                elif boards[ny][nx] == '.':
                    cnt += 1 
            
            if cnt >= 3:
                answers[y][x] = '.'
            else:
                answers[y][x] = 'X'
                sy = min(sy, y)
                sx = min(sx, x)
                ey = max(ey, y)
                ex = max(ex, x)

for y in range(sy, ey+1):
    for x in range(sx, ex+1):
        print(answers[y][x], end="")
    print()