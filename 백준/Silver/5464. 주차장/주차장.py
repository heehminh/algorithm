from collections import deque 
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())
cost = [int(input()) for _ in range(N)]
weight = [int(input()) for _ in range(M)]

dq = deque()
spaces = [0] * N

ans = 0

for i in range(2*M):
    num = int(input())
    
    if num > 0: # 입차 
        dq.append(num)
        
        while dq: 
            if 0 in spaces:
                w = dq.popleft()
                
                for k, v in enumerate(spaces):
                    if v == 0:
                        spaces[k] = w 
                        ans += weight[w-1] * cost[k]
                        break 
            
            else:
                break 
    
    else: # 출차
        car = -(num)
        for k, v in enumerate(spaces):
            if v == car:
                spaces[k] = 0
                break 
        
        if dq:
            w = dq.popleft()
            for k, v in enumerate(spaces):
                if v == 0:
                    spaces[k] = w 
                    ans += weight[w-1] * cost[k]
                    break

print(ans)