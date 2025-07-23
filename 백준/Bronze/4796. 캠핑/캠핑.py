import sys
input = sys.stdin.readline
cnt = 0

while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break 
    
    cnt += 1 
    ans = V//P * L
    if V%P > L:
        ans += L 
    else: 
        ans += V%P
    
    print(f"Case {cnt}: {ans}")