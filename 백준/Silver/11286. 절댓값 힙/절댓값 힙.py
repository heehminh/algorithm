import sys 
import heapq

input = sys.stdin.readline
h = []

N = int(input())

for _ in range(N):
    x = int(input())
    
    if x == 0:
        print(heapq.heappop(h)[1] if h else 0)
    
    else:
        heapq.heappush(h, [abs(x), x])