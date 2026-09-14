def solution(arr1, arr2):
    m = len(arr1) 
    n = len(arr1[0])
    r = len(arr2[0]) 
    
    answer = [[0] * r for _ in range(m)]
    
    for y in range(m): 
        for x in range(r): 
            num = 0
            for tmp in range(n):
                num += arr1[y][tmp] * arr2[tmp][x]
            
            answer[y][x] = num
    
    return answer 