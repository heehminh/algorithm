def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        if solve(s):
            answer += 1 
        s = str(s[1:] + s[0])
    
    return answer

def solve(word):
    stk = []
    ans = True 
    
    for w in list(word):
        if w in ['(', '[', '{']:
            stk.append(w)
            
        elif w in [')', ']', '}']:
            if stk:
                s = stk.pop()
                
                if (w == ')' and s != '(') or (w == ']' and s != '[') or (w == '}' and s != '{'):
                    ans = False
                    
            else:
                ans = False 
                
    if stk: 
        ans = False

    return ans 