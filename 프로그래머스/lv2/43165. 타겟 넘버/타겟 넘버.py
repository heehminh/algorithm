# 백트래킹 (DFS)
def solution(numbers, target):
    answer = 0 # 방법의 수 
    
    def dfs(idx, res):
        nonlocal answer 
        
        if idx == len(numbers):
            if res == target:
                answer += 1 
            return 
        
        dfs(idx+1, res+numbers[idx])
        dfs(idx+1, res-numbers[idx])
    
    dfs(0,0)
        
    return answer