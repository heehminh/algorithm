from collections import deque 

def solution(priorities, location):
    answer = []
    q = deque()
    
    for i in range(len(priorities)):
        q.append([priorities[i], i]) # 우선순위, 인덱스
    
    while q:
        num, idx = q.popleft()
        
        if q and max(q)[0] > num:
            q.append([num, idx])
        else:
            answer.append(idx)
    
    return answer.index(location) + 1