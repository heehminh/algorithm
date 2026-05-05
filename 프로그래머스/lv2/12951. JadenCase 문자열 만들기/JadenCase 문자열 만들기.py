def solution(s):
    s = s.title()
    answer = ''
    
    idx = 0 
    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1 
            answer += s[idx].lower()
            
        else:
            answer += s[idx]
        
        idx += 1 
    
    return answer 