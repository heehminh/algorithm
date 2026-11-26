from itertools import combinations 

def solution(orders, course):
    answer = []
    
    for cnt in course: 
        md = {}
        
        for idx in range(len(orders)):
            arr = sorted(list(orders[idx]))
            
            for combi in combinations(arr, cnt):
                k = "".join(combi)
                
                if k in md:
                    md[k] += 1 
                else:
                    md[k] = 1 
        
        if md and max(md.values()) > 1:
            for k, v in md.items():
                if max(md.values()) == v: 
                    answer.append(k)
    
    answer.sort()
    
    return answer