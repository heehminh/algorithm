def solution(a, b, n):
    answer = 0
    
    while (n > 1) and (n >= a):
        num = (n // a) * b
        remain = n % a
        answer += num 
        n = num + remain 
        
    return answer