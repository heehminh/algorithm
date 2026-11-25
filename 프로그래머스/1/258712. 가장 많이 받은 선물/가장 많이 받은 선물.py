from itertools import combinations

def solution(friends, gifts):
    answer = [0] * len(friends)
    
    arr = [[0] * len(friends) for _ in range(len(friends))]
    nd = {}
    for i in range(len(friends)):
        nd[friends[i]] = i 
    
    f = [0] * len(friends)
    
    for g in gifts:
        s, r = map(str, g.split(" "))
        s = nd[s]
        r = nd[r]
        
        arr[s][r] += 1 
        f[s] += 1
        f[r] -= 1 
    
    for combi in combinations(nd.values(), 2):
        a, b = combi
        if (arr[a][b] > 0 or arr[b][a] > 0) and arr[a][b] != arr[b][a]:
            if arr[a][b] > arr[b][a]:
                answer[a] += 1
            else:
                answer[b] += 1 
        
        else: 
            if f[a] > f[b]:
                answer[a] += 1
            elif f[a] < f[b]:
                answer[b] += 1
                
    return max(answer)