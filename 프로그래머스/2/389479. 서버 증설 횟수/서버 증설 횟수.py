import math

def solution(players, m, k):
    answer = 0 # 증설 횟수 
    s = [0] * 24 
    
    for i in range(len(players)):
        if players[i] > 0:
            cnt = max(math.floor((players[i] - (s[i]*m)) / m), 0)
            end_idx = min(24, i+k)
            for idx in range(i, end_idx):
                s[idx] += cnt 
            
            answer += cnt 
    
    return answer