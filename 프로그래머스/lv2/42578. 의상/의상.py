def solution(clothes):
    f_dict = {}
    answer = 1
    
    for name, type in clothes:
        if type in f_dict.keys():
            f_dict[type] += 1 
        else:
            f_dict[type] = 1 
    
    for _, v in f_dict.items():
        answer *= v+1 
    
    return answer-1