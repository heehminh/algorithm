# 백준 2346 풍선 터뜨리기
from collections import deque

N = int(input())
dq = deque(enumerate(map(int, input().split())))
result = [] 

while dq:
    idx, number = dq.popleft()
    result.append(idx+1)
    
    if number > 0:
        dq.rotate(-(number-1))
    elif number < 0:
        dq.rotate(-number)
        
print(" ".join(map(str, result)))