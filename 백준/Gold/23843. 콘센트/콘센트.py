import sys 
import heapq 
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(map(int, input().split()))

if M >= N:
    print(max(times))
else:
    times.sort(reverse=True) 
    
    h = [0] * M 
    heapq.heapify(h)
    
    for t in times:
        cur = heapq.heappop(h) # 가장 빨리 끝나는 콘센트 
        heapq.heappush(h, cur+t)
    
    print(max(h))