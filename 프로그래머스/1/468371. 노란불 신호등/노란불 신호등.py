import math

def solution(signals):
    answer = 0
    times = []
    
    s_dict = {}
    for i in range(len(signals)):        
        turn = [signals[i][0]+1, signals[i][0]+signals[i][1]]
        cycle = sum(signals[i])
        s_dict[i] = [turn, cycle]
        
        times.append(cycle)
    
    max_time = math.lcm(*times)
    
    while True:
        if answer > max_time:
            return -1 
        
        isYellow = True 
        for _, v in s_dict.items():
            turn = v[0]
            cycle = v[1]
            
            if not(answer % cycle >= turn[0] and answer % cycle <= turn[1]):
                isYellow = False         
        
        if isYellow:
            return answer 
        
        answer += 1 
    
    return answer