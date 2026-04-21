import sys 
from collections import deque

input = sys.stdin.readline
q = deque()
N = int(input())

for _ in range(N):
    com = list(map(str, input().split()))
    com_0 = com[0]
    
    if com_0 == 'push':
        q.append(com[1])
    
    elif com_0 == 'pop':
        print(q.popleft() if q else -1)
    
    elif com_0 == 'size':
        print(len(q))
    
    elif com_0 == 'empty':
        print(0 if q else 1)
    
    elif com_0 == 'front':
        print(q[0] if q else -1)
    
    elif com_0 == 'back':
        print(q[-1] if q else -1)