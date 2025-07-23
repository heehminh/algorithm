import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stk = [[] for _ in range(7)]
ans = 0

for _ in range(N):
    l, p = map(int, input().split()) # 줄, 프랫 
    
    while stk[l] and stk[l][-1] > p:
        stk[l].pop()
        ans += 1  
    
    if stk[l] and stk[l][-1] == p:
        continue 
    
    else:
        stk[l].append(p)
        ans += 1 

print(ans)