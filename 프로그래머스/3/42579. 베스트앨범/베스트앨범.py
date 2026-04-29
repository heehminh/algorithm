def solution(genres, plays):
    answer = []
    N = len(genres)
    
    gp_list = []
    for i in range(N):
        gp_list.append([genres[i], plays[i], i])
    
    gp_list.sort(key = lambda x: (-x[1], x[2]))
    
    g_dict = {}
    for i in range(N):
        if gp_list[i][0] in g_dict.keys():
            g_dict[gp_list[i][0]] += gp_list[i][1]
        else: 
            g_dict[gp_list[i][0]] = gp_list[i][1]
    
    sorted_g_dict = sorted(g_dict.items(), key = lambda x: -x[1])
    
    for k, v in sorted_g_dict:
        cnt = 0 
        for i in range(N):
            if cnt == 2:
                break 
            
            if gp_list[i][0] == k:
                cnt += 1 
                answer.append(gp_list[i][2])
        
    return answer