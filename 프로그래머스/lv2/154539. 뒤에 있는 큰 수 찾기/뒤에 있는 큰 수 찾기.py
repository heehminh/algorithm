def solution(numbers):
    answer = [-1] * len(numbers)
    stk = [] 
    
    for i in range(len(numbers)-1, -1, -1):
        while stk and stk[-1] <= numbers[i]:
            stk.pop()
        
        if stk:
            answer[i] = stk[-1]
        
        stk.append(numbers[i])
    
    return answer