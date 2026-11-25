def solution(bridge_length, weight, truck_weights):
    nxt = 0
    stk = [0] * bridge_length
    stk_sum = 0
    
    while stk:
        nxt += 1 
        s = stk.pop(0)
        stk_sum -= s 
        
        if truck_weights:
            if stk_sum + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                stk.append(t)
                stk_sum += t 
            else:
                stk.append(0)    
    
    return nxt