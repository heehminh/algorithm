def solution(n):
    div_set = set()
    
    for i in range(1, n+1):
        if n % i == 0:
            div_set.add(i)
            div_set.add(n/i)
    
    return sum(div_set)