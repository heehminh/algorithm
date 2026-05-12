import heapq 

def solution(book_time):
    book_time.sort(key=lambda x: x[0])
    
    s, e = book_time[0]
    
    b_s = int(s.split(":")[0]) * 60 + int(s.split(":")[1])
    b_e = int(e.split(":")[0]) * 60 + int(e.split(":")[1])
    
    rooms = [b_e]
    heapq.heapify(rooms)
    
    for idx in range(1, len(book_time)):
        s, e = book_time[idx]
        start = int(s.split(":")[0]) * 60 + int(s.split(":")[1])
        end = int(e.split(":")[0]) * 60 + int(e.split(":")[1])
        
        if rooms:
            before_end = heapq.heappop(rooms)
            
            if start >= before_end + 10:
                heapq.heappush(rooms, end)
            else:
                heapq.heappush(rooms, before_end)
                heapq.heappush(rooms, end)
            
        else:
            heapq.heappush(rooms, end)
    
    return len(rooms)
