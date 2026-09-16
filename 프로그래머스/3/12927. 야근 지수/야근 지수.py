import heapq

def solution(n, works):
    answer = 0
    
    h = []
    for w in works:
        h.append(-w)
    
    heapq.heapify(h)
    
    for i in range(n):
        w = heapq.heappop(h)
        
        if w == 0:
            return 0 
        
        heapq.heappush(h, w+1)
    
    for num in h:
        answer += num*num 
    
    return answer