def solution(number, k):
    stk = []
    
    for idx in range(len(number)):
        while stk and k > 0 and stk[-1] < number[idx]:  
            stk.pop()
            k -= 1 
        
        stk.append(number[idx])
    
    if k > 0:
        stk = stk[:len(number)-k]
    
    return "".join(stk) 

