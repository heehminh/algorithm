def solution(n):
    next_num = n+1
    
    while True:
        if format(n, 'b').count('1') == format(next_num, 'b').count('1'):
            return next_num
        
        next_num += 1 