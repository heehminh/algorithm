# 하루에 한시간 일하면 피로도 +A (일은 B만큼 처리)
# 한시간 쉬면 피로도 -C (음수면 0)
# 피로도 M 넘지않게 

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