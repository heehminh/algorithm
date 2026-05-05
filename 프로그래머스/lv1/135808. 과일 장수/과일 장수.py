def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    idx = 0 
    for i in range(len(score) // m):
        answer += min(score[idx:idx+m]) * m
        idx += m
    
    return answer