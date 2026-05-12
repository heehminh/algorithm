import heapq 

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0 
    
    while scoville:
        s1 = heapq.heappop(scoville)
        
        if s1 >= K:
            return answer 
        
        if scoville:
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, s1+s2*2)
        else:
            return -1
        
        answer += 1 
        
    return -1 
    