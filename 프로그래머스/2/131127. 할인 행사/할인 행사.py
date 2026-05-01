from collections import Counter 

def solution(want, number, discount):
    answer = 0
    
    for w in want:
        if w not in discount:
            return 0
    
    w = Counter(dict(zip(want, number)))
    day = sum(number)
    
    for i in range(len(discount)-day+1): 
        c = Counter(discount[i:i+day])

        if w == c:
            answer += 1     
    
    return answer