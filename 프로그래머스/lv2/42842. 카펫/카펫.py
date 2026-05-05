def solution(brown, yellow):
    w = brown // 2 + 2 - 3 
    h = 3 
    
    while w >= h:
        if w*h == brown+yellow:
            return [w, h]
        else:
            w -= 1 
            h += 1 