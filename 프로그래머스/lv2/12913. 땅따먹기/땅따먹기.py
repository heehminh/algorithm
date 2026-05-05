def solution(land):
    answer = 0 
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    
    return max(land[len(land)-1])
    

# 1 2 3 5 
# 9 10 11 12 # 같은 줄이 아닌 
# 12 14 15 16 -> 답 16 

