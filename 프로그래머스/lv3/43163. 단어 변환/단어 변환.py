# bfs 
# 각 단어의 길이는 3~10 

from collections import deque 

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0 
    
    def bfs(begin, target, words):
        dq = deque()
        dq.append((begin, 0)) # 시작 단어, 단계 
        
        while dq: 
            now, step = dq.popleft()
            
            # 종료조건 
            if now == target:
                return step 
        
            for word in words:
                cnt = 0 
                for i in range(len(word)):
                    if now[i] != word[i]:
                        cnt += 1 
                
                if cnt == 1: 
                    dq.append((word, step+1))

    return bfs(begin, target, words)