A, B, C, M = map(int, input().split())
p = 0
work = 0 
h = 0

while h < 24:
    if p + A > M:
        p = max(0, p-C) 
    else:
        p += A 
        work += B 
    h += 1 
    
print(work)