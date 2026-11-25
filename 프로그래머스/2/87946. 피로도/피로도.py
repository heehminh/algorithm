from itertools import permutations

def solution(k, dungeons): 
    answer = {0} # 초기값이 0인 set
    
    # [1] 정렬 
    dungeons.sort(key=lambda x: (-x[0], x[1]))
    
    # [2] 
    for permu in permutations(dungeons, len(dungeons)):
        tmp_ans = 0 
        tmp_k = k
        for m, c in permu: # 최소피로도, 소모피로도
            if tmp_k >= m:
                tmp_k -= c 
                tmp_ans += 1 
        
        answer.add(tmp_ans)
    
    return max(answer)