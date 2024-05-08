# 1번 카드가 제일 위에, N번 카드가 제일 아래에 
# 제일 위에 있는 카드를 버림, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 

from collections import deque 
q = deque()

N = int(input())

for i in range(N):
    q.append(i+1)

while(len(q) != 1):
    q.popleft() # 제일 위에 있는 카드 버림 
    q.append(q.popleft()) # 제일 위에 있는 카드 제일 아래에 넣기 

print(q.popleft())