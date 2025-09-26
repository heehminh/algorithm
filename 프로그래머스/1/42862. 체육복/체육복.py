def solution(n, lost, reserve):
    answer = 0
    
    arr = [1] * n
    
    for l in lost:
        arr[l-1] -= 1 
    
    for r in reserve:
        arr[r-1] += 1 
        
    for i in range(n):
        if i > 0 and arr[i] == 2:
            if arr[i-1] == 0:
                arr[i-1] += 1 
                arr[i] -= 1 
                    
        elif i < n-1 and arr[i] == 2:
            if arr[i+1] == 0:
                arr[i+1] += 1
                arr[i] -= 1 
                
    for c in arr:
        if c > 0:
            answer += 1 
    
    return answer # 1이상의 개수 