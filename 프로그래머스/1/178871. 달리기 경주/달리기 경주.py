def solution(players, callings):
    
    name_rank_dict = {}
    for i in range(len(players)):
        name_rank_dict[players[i]] = i # 이름: 등수 
    
    
    for name in callings:
        i = name_rank_dict[name]
        prev = players[i-1]
        
        players[i] = players[i-1]
        players[i-1] = name 
        
        name_rank_dict[name] -= 1 
        name_rank_dict[prev] += 1 
        
    return players