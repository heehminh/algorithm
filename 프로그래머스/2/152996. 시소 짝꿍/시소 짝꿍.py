from itertools import combinations 

def solution(weights):
    answer = 0
    weights.sort()
    
    wd = {}
    for w in weights:
        if w in wd:
            wd[w] += 1 
        else:
            wd[w] = 1 
    
    for cnt in wd.values():
        answer += cnt*(cnt-1) // 2
    
    for small, big in combinations(wd.keys(), 2):
        arr = [small*2, small*3/2, small*4/3]
        # 180, 360, 270, 240 
        if big in arr:
            answer += wd[small] * wd[big]
        
    return answer