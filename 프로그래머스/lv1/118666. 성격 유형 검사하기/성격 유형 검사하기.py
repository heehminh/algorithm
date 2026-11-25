def solution(survey, choices):
    answer = ''
    choice_dict = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    
    def append_answer(A, B):
        if choice_dict[A] >= choice_dict[B]:
            return A
        else:
            return B
    
    for i in range(len(choices)):
        if choices[i] > 4:
            choice_dict[survey[i][1]] += choices[i] - 4
        else:
            choice_dict[survey[i][0]] += 4 - choices[i]
            
    answer += append_answer('R', 'T')
    answer += append_answer('C', 'F')
    answer += append_answer('J', 'M')
    answer += append_answer('A', 'N')
    
    return answer

