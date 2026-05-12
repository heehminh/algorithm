from itertools import combinations 

def solution(orders, course):
    answer = []
    
    for n in course:
        o_dict = {}
        for o in orders:
            for combi in combinations(o, n):
                key = ''.join(list(sorted(combi)))
                
                if key in o_dict:
                    o_dict[key] += 1 
                else:
                    o_dict[key] = 1 
        
        if o_dict:
            max_num = max(max(o_dict.values()), 2)
            for k, v in o_dict.items():
                if v == max_num:
                    answer.append(k)
            
    return sorted(answer)