import heapq
import sys 
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[0], x[1]))
min_h = [] # 종료시간

cnt = 1 
for s, t in arr:
    if min_h and min_h[0] <= s:
        heapq.heappop(min_h)
    
    heapq.heappush(min_h, t)

print(len(min_h))