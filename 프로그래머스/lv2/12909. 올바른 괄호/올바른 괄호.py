def solution(s):
    answer = True
    s_ = list(s)
    stk = []
    
    for item in s_:
        if item == '(':
            stk.append(item)
        elif len(stk) == 0 and item == ')':
            answer = False 
            break
        else:
            stk.pop()
    
    if len(stk) > 0:
        answer = False 

    return answer