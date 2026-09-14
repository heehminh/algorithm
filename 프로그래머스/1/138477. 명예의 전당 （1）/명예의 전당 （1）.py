def solution(k, score):
    answer = []
    result = []
    
    for i in range(len(score)):
        answer.append(score[i])
        answer.sort(reverse=True)
        
        if len(answer) >= k:
            result.append(answer[k-1])
        else:
            result.append(answer[-1])
    
    return result