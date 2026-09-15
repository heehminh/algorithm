def solution(clothes):
    answer = 1
    c_dict = {}
    
    for _, k in clothes:
        if k in c_dict:
            c_dict[k] += 1 
        else: 
            c_dict[k] = 1 
    
    for v in c_dict.values():
        answer *= (v+1)
    
    return answer-1