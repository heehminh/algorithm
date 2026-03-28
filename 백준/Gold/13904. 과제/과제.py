import sys 
import heapq 

input = sys.stdin.readline
h = []

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(reverse=True)

max_day = arr[0][0]
ans = 0 
idx = 0 

for day in range(max_day, 0, -1):
    # day에 수행가능한 과제를 힙에 넣음
    while idx < N and arr[idx][0] >= day:
        heapq.heappush(h, -arr[idx][1]) # 최대힙처럼
        idx += 1 
    
    # 그날 할 수 있는 과제 중 가장 점수가 큰 것 수행
    if h:
        ans += -heapq.heappop(h)

print(ans)