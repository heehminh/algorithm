from collections import deque 
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())

dq = deque()

for i in range(1, N+1):
    dq.append(i)

arr = list(map(int, input().split()))
ans = 0 

for i in arr:
    while True:
        if dq[0] == i:
            dq.popleft()
            break 
        else: 
            if dq.index(i) < len(dq)/2: 
                while dq[0] != i:
                    dq.append(dq.popleft())
                    ans += 1 
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    ans += 1 

print(ans)