import sys 
input = sys.stdin.readline 

N = int(input())
M = int(input())
if M > 0:
    broken = list(input().split())
else:
    broken = []
    
ans = abs(100-N) # 현재 채널에서 +, - 만 사용하여 이동 

for num in range(500000*2 + 1):
    isBroken = False  
    n = str(num)
    
    for ch in n:
        # 숫자가 고장났는지 
        if ch in broken:
            isBroken = True 
            break 
    
    if not isBroken:
        # len(n): 숫자를 누른 횟수, abs(N-num): +/- 이동횟수
        ans = min(ans, len(n) + abs(N-num)) 

print(ans)