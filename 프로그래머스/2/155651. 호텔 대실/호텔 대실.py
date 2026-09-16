import heapq

def solution(book_time):
    answer = []
    
    mList = []
    for s, e in book_time:
        sh, sm = s.split(":")
        eh, em = e.split(":")
        
        mList.append([int(sh)*60 + int(sm), int(eh)*60 + int(em)])
    
    mList.sort()
    
    h = []
    for s, e in mList:
        if h and h[0] <= s:
            heapq.heappop(h)
        
        heapq.heappush(h, e+10)
    
    return len(h)