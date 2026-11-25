def solution(s):
    answer = True
    
    stk = []
    
    for idx in range(len(s)):
        if s[idx] == '(':
            stk.append('(')
        
        elif s[idx] == ')' and stk:
            stk.pop()
        
        else:
            return False 
    
    if stk:
        return False 

    return True