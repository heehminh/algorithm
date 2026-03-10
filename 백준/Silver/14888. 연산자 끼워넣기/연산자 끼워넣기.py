import math 
import sys 
input = sys.stdin.readline 

N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split())) # +, -, *, / 

max_ans = -math.inf 
min_ans = math.inf

def dfs(idx, value):
    global max_ans, min_ans 
    
    if idx == N:
        max_ans = max(max_ans, value)
        min_ans = min(min_ans, value)
        return 

    if op[0] > 0:
        op[0] -= 1 
        dfs(idx+1, value+arr[idx])
        op[0] += 1 
    
    if op[1] > 0:
        op[1] -= 1 
        dfs(idx+1, value-arr[idx])
        op[1] += 1 
    
    if op[2] > 0:
        op[2] -= 1
        dfs(idx+1, value*arr[idx])
        op[2] += 1 
    
    if op[3] > 0:
        op[3] -= 1 
        
        if value >= 0:
            dfs(idx+1, value//arr[idx])
        else: # C++기준 
            dfs(idx+1, (abs(value)//arr[idx])*-1)
        
        op[3] += 1 

dfs(1, arr[0])

print(max_ans)
print(min_ans)