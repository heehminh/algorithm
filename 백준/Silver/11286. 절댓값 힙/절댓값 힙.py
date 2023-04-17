# 배열에 정수 x를 넣는다
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다
# 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고 그 값을 제거한다
import heapq
import sys

N = int(input())
pq = []
for i in range(N):
    num = int(sys.stdin.readline())
    if (num == 0):
        if (pq):
            print(heapq.heappop(pq)[1])
        else: 
            print(0)
    else:
        heapq.heappush(pq, (abs(num), num))