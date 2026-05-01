def solution(n):
    next_num = n+1
    
    while True:
        if bin(n).count('1') == bin(next_num).count('1'):
            return next_num
        
        next_num += 1 