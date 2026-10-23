def solution(s):
    answer = 1
    
    word = list(s)
    i = 1 
    
    lcnt = 1 
    rcnt = 0 
    
    x = word[0]
    
    while i < len(word):
        if lcnt == rcnt:
            answer += 1 
            lcnt = 1 
            rcnt = 0 
            x = word[i]
            
        else:
            if word[i] == x:
                lcnt += 1 
            else:
                rcnt += 1 
        
        i += 1 
    
    return answer