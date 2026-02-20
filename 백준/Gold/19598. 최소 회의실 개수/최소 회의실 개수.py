import heapq
import sys 
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

h = []

for s, e in arr:
    if h and h[0] <= s:
        heapq.heappop(h)
    
    heapq.heappush(h, e)

print(len(h))