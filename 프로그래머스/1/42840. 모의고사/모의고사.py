def solution(answers):
    
    p = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == p[0][i%5]:
            scores[0] += 1 
        
        if answers[i] == p[1][i%8]:
            scores[1] += 1 
        
        if answers[i] == p[2][i%10]:
            scores[2] += 1 
    
    answer = []
    
    for idx in range(3):
        if scores[idx] == max(scores):
            answer.append(idx+1)
    
    return answer 
    