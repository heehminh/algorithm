N, K = map(int, input().split())

dict = {}
ans = 0 

for i in range(N):
    s, y = map(int, input().split())
    
    if (s,y) in dict.keys():
        dict[(s,y)] += 1 
        if dict[(s,y)] > K:
            ans += 1 
            dict[(s,y)] -= K
        
    else:
        dict[(s,y)] = 1
        ans += 1 
        
print(ans)