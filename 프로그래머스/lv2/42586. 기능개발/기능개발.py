def solution(progresses, speeds):
    import math
    
    answer = []
    
    end_days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i]) # 각 작업이 언제 끝나는지 
        end_days.append(day)
    
    cnt = 1 
    before_day = end_days[0]
    
    for i in range(1, len(end_days)):
        if end_days[i] <= before_day:
            cnt += 1 
        else:
            answer.append(cnt)
            cnt = 1 
            before_day = end_days[i]
    
    answer.append(cnt) # 마지막 묶음 추가 
    
    return answer