def solution(s):
    answer = []
    
    before_char_dict = {}
    
    for idx in range(len(s)):
        if s[idx] in before_char_dict.keys():
            answer.append(idx - before_char_dict[s[idx]])     
        else:
            answer.append(-1)
        before_char_dict[s[idx]] = idx 
    
    return answer