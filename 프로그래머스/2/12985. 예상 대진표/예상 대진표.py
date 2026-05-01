import math 

def solution(n,a,b):
    answer = 0
    dp = []
    max_round = int(math.log(n, 2))
    num = 2
    
    for r in range(1, max_round+1):
        tmp_list = [r]
        for idx in range(1, n+1, num):
            tmp_list.append([i for i in range(idx,idx+num)])
        dp.append(tmp_list)
        num *= 2 
    
    for i in range(len(dp)):  
        r = dp[i][0]
        for num_list in dp[i][1:]:
            if a in num_list and b in num_list:
                return r 