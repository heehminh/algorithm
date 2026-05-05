def solution(nums):
    n = len(nums)/2 #nums는 항상 짝수 
    
    sets = set(nums)
    if len(sets) >= n:
        answer = n
    else:
        answer = len(sets) 
    
    return answer