import sys
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]
    
    ans = True 
    arr.sort()
    
    for i in range(N-1):
        if arr[i+1].startswith(arr[i]):
            ans = False 
            break 
    
    print('YES' if ans else 'NO')
