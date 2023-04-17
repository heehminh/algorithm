from collections import deque
q = deque()
N = int(input())
for i in range(1, N+1):
    q.append(i)

while len(q)>1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())