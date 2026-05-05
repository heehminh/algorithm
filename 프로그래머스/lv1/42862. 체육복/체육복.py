def solution(n, lost, reserve):
    l = set(lost) - set(reserve)
    r = set(reserve) - set(lost)

    for p in sorted(r):
        if p-1 in l:
            l.remove(p-1)
        
        elif p+1 in l:
            l.remove(p+1)
    
    return  n-len(l) 