import heapq 
import sys
input = sys.stdin.readline 

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[1]) # 시작시간 기준 정렬 
h = []

for _, s, e in arr:
    if h and h[0] <= s:
        heapq.heappop(h)
    
    heapq.heappush(h, e)

print(len(h))

