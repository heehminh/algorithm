def solution(clothes):
    answer = 1
    cd = {}
    
    for cn, ct in clothes:
        if ct in cd: 
            cd[ct] += 1 
        else:
            cd[ct] = 1 
    
    for t, n in cd.items():
        answer *= (n+1)
    
    return answer - 1 