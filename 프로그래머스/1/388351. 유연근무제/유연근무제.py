def solution(schedules, timelogs, startday):
    answer = 0 
    
    for i in range(len(schedules)):
        dead_time = schedules[i] + 10 
        
        if (schedules[i] + 10)%100 >= 60:
            dead_time = schedules[i] + 10 - 60 + 100 
        
        day = startday 
        isPass = True 
        
        for time in timelogs[i]:
            if day not in [6,7] and time > dead_time:
                isPass = False 
                break 
                
            day += 1 
            if day > 7:
                day = 1 
    
        if isPass:
            answer += 1 
    
    return answer