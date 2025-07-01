def solution(wallet, bill):
    answer = 0
    min_num = min(wallet[0], wallet[1])
    max_num = max(wallet[0], wallet[1])
        
    while (min(bill[0], bill[1]) > min_num) or (max(bill[0], bill[1]) > max_num):
        if bill[0] > bill[1]:
            bill[0] //= 2
            
        else:
            bill[1] //= 2
        
        answer += 1 
            
    return answer