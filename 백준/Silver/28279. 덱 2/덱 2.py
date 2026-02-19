from collections import deque
import sys 

input = sys.stdin.readline
dq = deque()
N = int(input())

for i in range(N):
    commands = list(map(int, input().split()))
    c = commands[0]
    
    if c == 1:
        dq.appendleft(commands[1])
    
    elif c == 2:
        dq.append(commands[1])
    
    elif c == 3:
        print(dq.popleft() if dq else -1)
    
    elif c == 4:
        print(dq.pop() if dq else -1)
    
    elif c == 5:
        print(len(dq))
    
    elif c == 6:
        print(0 if dq else 1)
    
    elif c == 7:
        print(dq[0] if dq else -1)
    
    elif c == 8:
        print(dq[-1] if dq else -1)