import math
def solution(progresses, speeds):
    days = []
    answer = []
    
    # 완성까지 며칠 걸리는지 계산 
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    b = days[0]
    num = 1 
    
    for i in range(1, len(days)):
        if b >= days[i]:
            num += 1 
        else:
            b = days[i]
            answer.append(num)
            num = 1
    
    answer.append(num)
    
    return answer