# 백준 2164 카드2 - 큐
# 123456 
# 3456 2
# 562 4
# 24 6
# 6 4
# 4 

# 큐로 풀이 
from collections import deque
q = deque()
N = int(input())
for i in range(1, N+1):
    q.append(i)

while len(q)>1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())
    