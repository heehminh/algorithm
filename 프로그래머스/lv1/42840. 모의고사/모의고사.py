def solution(answers):
    scores =  [0, 0, 0]
    p = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for idx in range(len(answers)):
        for k in range(3):
            if answers[idx] == p[k][idx % len(p[k])]:
                scores[k] += 1
    
    max_score = max(scores)
    
    return [i+1 for i, s in enumerate(scores) if s == max_score]
    