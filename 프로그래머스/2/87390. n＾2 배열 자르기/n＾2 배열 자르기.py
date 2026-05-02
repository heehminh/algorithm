def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        y = i // n
        x = i % n 
        answer.append(max(y,x)+1)
    
    return answer
    
#     시간초과 
#     # [1] n*n 2차원 배열 
#     nxn_array = [[0] * n for _ in range(n)]
    
#     # [2] 배열에 숫자 채우기 
#     for y in range(n):
#         for x in range(n):
#             nxn_array[y][x] = max(y, x) + 1
            
#     # [3] 새로운 2차원 배열 (arr)
#     arr = []
#     for i in range(n):
#         for j in range(n):
#             arr.append(nxn_array[j][i])
    
#     # [4] arr[left] ~ arr[right]
#     return arr[left:right+1]