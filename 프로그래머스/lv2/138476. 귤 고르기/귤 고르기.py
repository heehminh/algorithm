from collections import Counter 

def solution(k, tangerine):
    answer = 0 
    
    c = Counter(tangerine).values()
    v = sorted(c, reverse=True)
    
    i = 0
    while k > 0:
        k -= v[i]
        answer += 1 
        i += 1 

    return answer