import heapq 

def solution(cacheSize, cities):
    answer = 0
    t = 0 
    h = []
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for idx in range(len(cities)):
        c = cities[idx]
        c = c.lower()
        
        isCached = False 
        
        tmp = []
        for _ in range(len(h)):
            ot, oc = heapq.heappop(h)
            tmp.append([ot, oc])
        
        for old in tmp:
            ot, oc = old
            
            if oc == c:
                heapq.heappush(h, (idx, c))
                isCached = True 
                
            else:
                heapq.heappush(h, (ot, oc))
        
        if isCached:
            answer += 1 
            
        else:
            if len(h) >= cacheSize:
                heapq.heappop(h)

            heapq.heappush(h, (idx, c))
            answer += 5 
            
    return answer