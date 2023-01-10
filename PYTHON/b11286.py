# 백준 11286 절댓값 힙

import heapq
import sys # 시간초과로 인한 빠른 입력 

pq = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        # 배열에 x라는 값을 추가하는 연산
        heapq.heappush(pq, (abs(x), x))
    else:
        # 배열에서 '절댓값'이 가장 작은 값을 출력하고 제거
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)