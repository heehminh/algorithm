import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    
    ans = 1 
    b = arr[0][1]
    
    for i in range(1, N):        
        if arr[i][1] < b:
            ans += 1 
            b = arr[i][1]
    
    print(ans)