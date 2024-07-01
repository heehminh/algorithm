# 백준 18258 큐 2 
import sys 
from collections import deque

dq = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    method = sys.stdin.readline().split()
    
    if method[0] == "push":
        dq.append(method[1])
        
    elif method[0] == "pop":
        print(dq.popleft() if dq else -1)
        
    elif method[0] == "size":
        print(len(dq))
        
    elif method[0] == "empty":
        print(0 if dq else 1)
        
    elif method[0] == "front":
        print(dq[0] if dq else -1)
        
    elif method[0] == "back":
        print(dq[-1] if dq else -1)