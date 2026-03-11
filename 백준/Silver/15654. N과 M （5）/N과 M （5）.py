import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

chk = [False] * (N)
res = []

def dfs():
    if len(res) == M:
        print(*res)
        return 
    
    for nxt in range(N):
        if not chk[nxt]:
            chk[nxt] = True 
            res.append(arr[nxt])
            
            dfs()
            
            res.pop()
            chk[nxt] = False 

dfs()