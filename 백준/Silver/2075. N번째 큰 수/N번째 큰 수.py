import sys 
import heapq 

input = sys.stdin.readline

N = int(input())
h = [] # 크기가 N 이하인 최소힙 

for _ in range(N):
    for x in map(int, input().split()):
        if len(h) < N: 
            heapq.heappush(h, x)
        else:
            if x > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, x)

print(h[0])