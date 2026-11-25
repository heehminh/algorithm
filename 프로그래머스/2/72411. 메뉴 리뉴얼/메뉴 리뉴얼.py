from itertools import combinations 

def solution(orders, course):
    answer = []
    
    for cnt in course:
        cd = {}
        
        for o in orders: 
            for combi in combinations(list(o), cnt):
                cc = "".join(sorted(combi))
                
                if cc in cd:
                    cd[cc] += 1 
                else:
                    cd[cc] = 1 
        
        
        sarr = []
        for k, v in sorted(cd.items(), reverse=True, key=lambda x: x[1]):
            s = ''
            for i in range(cnt):
                s += k[i]
            
            sarr.append([v, s])
            max_value = max(sarr[0][0], 2)
        
        for v, n in sarr:
            if v == max_value:  
                answer.append("".join(sorted(n))) # 넣을때 알파벳 오름차순으로 정렬해서 넣기  
    
    answer.sort()
    
    return answer