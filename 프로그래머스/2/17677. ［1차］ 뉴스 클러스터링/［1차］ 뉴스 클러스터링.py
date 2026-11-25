def solution(str1, str2):
    answer = 0
    
    wd = {}
    
    s1 = []
    s2 = []
    
    for idx in range(len(str1)):
        s1.append(str1[idx].lower())
    
    for idx in range(len(str2)):
        s2.append(str2[idx].lower())
    
    for idx in range(len(s1)-1):
        k = s1[idx] + s1[idx+1]
        if k.isalpha():
            if k in wd:
                wd[k][0] += 1 

            else:
                wd[k] = [1, 0]
    
    for idx in range(len(s2)-1):
        k = s2[idx] + s2[idx+1]
        
        if k.isalpha():
            if k in wd:
                wd[k][1] += 1 

            else:
                wd[k] = [0, 1]
    
    if len(wd) == 0:
        return 65536

    cnt = 0 
    wsum = 0 
    
    for k, v in wd.items():
        v1, v2 = v 
        wsum += max(v1, v2)
        
        if (v1 != 0 and v2 != 0):
            cnt += min(v1, v2)
    
    answer = cnt / wsum
    
    return int(answer * 65536)