import heapq 

def solution(operations):
    answer = []
    h = []
    
    for o in operations:
        c, num = o.split(" ")
        
        if c == 'I':
            heapq.heappush(h, int(num))
            
        elif h:
            if num == '1': # 최댓값 삭제 
                h.remove(max(h))
            else: # 최솟값 삭제 
                heapq.heappop(h)
    
    return [max(h), min(h)] if h else [0,0]