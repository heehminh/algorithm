def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    id_mapping = {}
    i_dict = {}
    
    for idx in range(len(id_list)):
        i_dict[id_list[idx]] = [0, []] 
        id_mapping[id_list[idx]] = idx 
    
    for r in report:
        a, b = r.split(" ")
        
        if a not in i_dict[b][1]:
            i_dict[b][0] += 1 
            i_dict[b][1].append(a)
            
            
    for _, v in i_dict.items():
        cnt = v[0]
        
        if cnt >= k:
            for n in v[1]:
                answer[id_mapping[n]] += 1 
                
    return answer