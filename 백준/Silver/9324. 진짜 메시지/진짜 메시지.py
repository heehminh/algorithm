T = int(input())

for _ in range(T):
    m = list(input())

    cnt = {}
    ans = True 
    i = 0 
    
    while i < len(m):
        if m[i] in cnt:
            cnt[m[i]] += 1 
        else:
            cnt[m[i]] = 1 
        
        if cnt[m[i]] % 3 == 0:
            if i == len(m)-1 or m[i] != m[i+1]:
                ans = False 
                break 
            i += 2 
        else:
            i += 1 
    
    print('OK') if ans else print('FAKE')