import sys
import heapq

pq = [] # 절댓값, 값을 넣고 출력할때는 값만 출력 
N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if (num == 0):
        if pq: print(heapq.heappop(pq)[1])
        else: print(0)
    else: 
        heapq.heappush(pq, (abs(num), num))