# 주차장
from collections import deque

N, M = map(int, input().split())

costs = [int(input()) for _ in range(N)]
weights = [int(input()) for _ in range(M)]

cars = [int(input()) for _ in range(2 * M)]

ans = 0 # 총 요금

space = [0 for _ in range(N)] # 주차 공간 초기화 (0은 빈 공간)
dq = deque() # 대기 큐

for num in cars:
    if num > 0: # 입차
        dq.append(num) # 대기 큐에 차량 추가
        
        while dq:
            if 0 in space: # 빈 공간이 있을 때
                w = dq.popleft() # 가장 오래 대기한 차량 꺼내기
                
                for idx, spot in enumerate(space):
                    if spot == 0:
                        space[idx] = w # 차량 주차
                        ans += weights[w - 1] * costs[idx] # 요금 계산
                        break
            else:
                break # 빈 공간이 없으면 대기
    
    else: # 출차
        out_car = abs(num)
        for idx, spot in enumerate(space):
            if spot == out_car:
                space[idx] = 0 # 차량 출차 후 공간 비우기
                break
        
        if dq: # 대기 중인 차량이 있을 때
            w = dq.popleft() # 대기 중인 차량 꺼내기
            for idx, spot in enumerate(space):
                if spot == 0:
                    space[idx] = w # 차량 주차
                    ans += weights[w - 1] * costs[idx] # 요금 계산
                    break

print(ans)
