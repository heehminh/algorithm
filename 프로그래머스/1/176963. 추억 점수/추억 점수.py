def solution(name, yearning, photo):
    answer = []
    score_dict = {}
    
    for idx in range(len(name)):
        score_dict[name[idx]] = yearning[idx]
    
    for p in photo:
        result = 0 
        for item in p:
            if item in score_dict.keys():
                result += score_dict[item]
        answer.append(result)
    
    return answer