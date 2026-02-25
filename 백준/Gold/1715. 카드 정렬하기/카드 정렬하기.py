import heapq 
import sys 
input = sys.stdin.readline

N = int(input())
h = [int(input()) for _ in range(N)]
heapq.heapify(h)

if N == 1:
    print(0)
    exit()

ans = 0 
while len(h) > 1:
    sum = heapq.heappop(h) + heapq.heappop(h) # 가장 작은 두개 
    ans += sum 
    heapq.heappush(h, sum)

print(ans)