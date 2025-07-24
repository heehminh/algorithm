def solution(answers):
    a, b, c = 0, 0, 0
    
    for i in range(len(answers)):
        
        if answers[i] == 1:
            if (i+1) % 5 == 1:
                a += 1 
                
            if i % 8 == 1:
                b += 1 
                
            if i % 10 == 2 or i % 10 == 3:
                c += 1 
        
        elif answers[i] == 2:
            if (i+1) % 5 == 2:
                a += 1 
            
            if i % 2 == 0:
                b += 1 
                
            if i % 10 == 4 or i % 10 == 5:
                c += 1 
                
        elif answers[i] == 3:
            if (i+1) % 5 == 3:
                a += 1 
            
            if i % 8 == 3:
                b += 1 
                
            if i % 10 == 0 or i % 10 == 1:
                c += 1 
    
        elif answers[i] == 4:
            if (i+1) % 5 == 4:
                a += 1 
            
            if i % 8 == 5:
                b += 1 
                
            if i % 10 == 6 or i % 10 == 7:
                c += 1 
                
        elif answers[i] == 5:
            if (i+1) % 5 == 0:
                a += 1 
            
            if i % 8 == 7:
                b += 1 
                
            if i % 10 == 8 or i % 10 == 9:
                c += 1 
        
    answer = []
    answer.append([1,a])
    answer.append([2,b])
    answer.append([3,c])
    answer.sort(key = lambda x: x[1], reverse=True)
    max_answer = 0 
    
    for ans in answer:
        max_answer = max(max_answer, ans[1])
        
    result = []
    for res in answer:
        if res[1] == max_answer:
            result.append(res[0])
    
    return result