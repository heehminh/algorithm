def solution(dirs):
    answer = 0
    
    sy = 0
    sx = 0 
    
    y_chk = [[False] * 11 for _ in range(11)] # 세로 체크배열
    x_chk = [[False] * 11 for _ in range(11)] # 가로 체크배열 

    def is_valid_coord(y,x):
        return -5 <= y <= 5 and -5 <= x <= 5 
    
    for d in dirs:
        ay, ax = sy+5, sx+5
        
        if d == 'U':
            if is_valid_coord(sy+1,sx) and not y_chk[ay][ax]:
                y_chk[ay][ax] = True
                answer += 1 
            sy = min(5, sy+1)
            
        elif d == 'D':
            if is_valid_coord(sy-1,sx) and not y_chk[ay-1][ax]:
                y_chk[ay-1][ax] = True
                answer += 1 
            sy = max(-5, sy-1) 
            
        elif d == 'R':
            if is_valid_coord(sy,sx+1) and not x_chk[ay][ax]:
                x_chk[ay][ax] = True
                answer += 1 
            sx = min(5, sx+1)
            
        elif d == 'L':            
            if is_valid_coord(sy,sx-1) and not x_chk[ay][ax-1]:
                x_chk[ay][ax-1] = True
                answer += 1 
            sx = max(-5, sx-1)

    return answer