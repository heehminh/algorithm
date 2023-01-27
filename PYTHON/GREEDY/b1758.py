# 백준 1758 알바생 강호
import sys

N = int(sys.stdin.readline())
tips = [int(input()) for _ in range(N)]
tips.sort()
tips.reverse()

ans = 0
cnt = 1
for i in tips:
    tip = i - (cnt-1)
    if tip <= 0: 
        tip = 0
    ans += tip
    cnt += 1
    
print(ans)
