def solution(n, lost, reserve):
    arr = [1] * n 
    
    for l in lost:
        arr[l-1] -= 1 
    
    for r in reserve:
        arr[r-1] += 1 
    
    
    for idx in range(n):
        if arr[idx] > 1:
            if idx > 0 and arr[idx-1] == 0:
                arr[idx-1] += 1 
                arr[idx] -= 1 
            
            elif idx < n-1 and arr[idx+1] == 0:
                arr[idx+1] += 1
                arr[idx] -= 1 
    
    answer = 0
    for num in arr:
        if num > 0: 
            answer += 1 
    
    return  answer 