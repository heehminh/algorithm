N, M = map(int, input().split())
arr = []

def dfs():
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return 
    
    for i in range(N):
        if i+1 not in arr:
            arr.append(i+1)
            dfs()
            arr.pop()
            
dfs()