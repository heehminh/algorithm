import heapq 

def solution(scoville, K):
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    
    answer = 0 
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            return answer 
        
        if len(scoville) < 2:
            return -1 
        
        temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, temp)
        answer += 1 
        
    return answer 
    